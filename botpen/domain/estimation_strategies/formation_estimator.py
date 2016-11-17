from collections import namedtuple
from domain.models import Estimation
import math

Coordinate = namedtuple('Coordinate', 'agent x y r theta')

class FormationEstimator:
    def __init__(self, estimation_repo):
        self.estimation_repo = estimation_repo
        self.name = "Formation"

    def setup(self, config):
        for agent in config['agents']:
            self.estimation_repo.update(
                Estimation(
                    agent['id'],
                    agent['x0'],
                    agent['y0'],
                    agent['theta0']))

    def estimate(self, moves, observations):
        #initial estimation from odometry
        estimates = observations.odometries
        odometric = {}
        for agent_id in estimates:
            last = self.estimation_repo.get(agent_id)
            obs = observations.odometries[agent_id]

            #the observed positions using previous estimation
            odometric[agent_id] = Estimation(
                agent_id = agent_id,
                x = last.x + obs.dx,
                y = last.y + obs.dy,
                theta = last.theta + obs.dtheta
            )
        (odometric_c, (cx,cy)) = _shift2centroid(odometric.values())

        #normalize the ranges
        ranges = observations.ranges
        poses = {}
        for agent_id in ranges:
            poses[agent_id] = Estimation(
                agent_id = agent_id,
                x = ranges[agent_id].dx,
                y = ranges[agent_id].dy,
                theta = ranges[agent_id].dtheta
            )
        (poses, _) = _shift2centroid(poses.values())

        #find the optimal angle
        agent_ids = odometric_c.keys()
        run = 0
        rise = 0

        for agent_id in agent_ids:
            o = odometric_c[agent_id]
            p = poses[agent_id]

            run += o.r * p.r * math.cos(p.theta - o.theta)
            rise += o.r * p.r * math.sin(p.theta - o.theta)

        phi = math.atan2(rise, run)

        results = {}
        diff = 0
        for agent_id in agent_ids:
            p = poses[agent_id]
            o = poses[agent_id]
            estimate = Estimation(
                agent_id = agent_id,
                x = p.r * math.cos(p.theta + phi) + cx,
                y = p.r * math.sin(p.theta + phi) + cy,
                theta = ranges[agent_id].dtheta + phi
            )

            self.estimation_repo.update(estimate)

            results[agent_id] = estimate
            diff1 = math.pow(o.x - estimate.x,2) + math.pow(o.y - estimate.y, 2)

        return {
            'estimates':results,
            'centroid_x': cx,
            'centroid_y': cy,
            'odometric': odometric}

def _shift2centroid(estimates):
    results = {}

    #get the centroids
    total_x = 0
    total_y = 0
    total_count = len(estimates)

    for estimate in estimates:
        total_x += estimate.x
        total_y += estimate.y

    centroid_x = total_x/total_count
    centroid_y = total_y/total_count

    #get the positions in the centroid frame
    for estimate in estimates:
        agent_id = estimate.agent_id
        x = estimate.x - centroid_x
        y = estimate.y - centroid_y

        r = math.sqrt(math.pow(x,2) + math.pow(y,2))
        theta = math.atan2(y,x)

        results[agent_id] = Coordinate(
                agent = agent_id,
                x = x,
                y = y,
                r = r,
                theta = theta
            )

    return (results, (centroid_x, centroid_y))
