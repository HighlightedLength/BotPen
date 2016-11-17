from domain.models import Estimation

class OdometryEstimator:
    def __init__(self, estimation_repo):
        self.estimation_repo = estimation_repo
        self.name = "Odometry"

    def setup(self, config):
        for agent in config['agents']:
            self.estimation_repo.update(
                Estimation(
                    agent['id'],
                    agent['x0'],
                    agent['y0'],
                    agent['theta0']))

    def estimate(self, moves, observations):
        result = {}
        for agent_id in observations.odometries:
            last = self.estimation_repo.get(agent_id)
            obs = observations.odometries[agent_id]
            estimation = Estimation(
                agent_id = agent_id,
                x = last.x + obs.dx,
                y = last.y + obs.dy,
                theta = last.theta + obs.dtheta
            )
            self.estimation_repo.update(estimation)
            result[agent_id] = estimation

        return result
