from domain.models import Estimation
import pykalman
import scipy.sparse as sp
import numpy as np
from botpen.util import elf

class KalmanEstimator:
    name = "Kalman"
    prev_state = None
    prev_covariance = None
    kf = None

    def setup(self, config):
        agents = config['agents']
        defaults = config['agent_defaults']
        agent_count = len(config['agents'])

        transition_matrix = np.array(np.eye(agent_count * 3)).tolist()
        observation_matrix = _build_observation_matrix(agent_count)

        actuation_noise = sum([
            [   elf.get_default('actuation_noise_x', agent, defaults),
                elf.get_default('actuation_noise_y', agent, defaults),
                elf.get_default('actuation_noise_theta', agent, defaults),]
                for agent in config['agents']],
            [])
        transition_covariance = sp.diags(actuation_noise).todense()

        observation_noise = sum([
            [   elf.get_default('observation_noise_x', agent, defaults),
                elf.get_default('observation_noise_y', agent, defaults),
                elf.get_default('observation_noise_theta', agent, defaults),]
            for agent in config['agents']],
            [])
        observation_noise.extend([0]*(3*agent_count -3))
        observation_covariance = sp.diags(observation_noise).todense()

        transition_offsets = [0]*(3*agent_count)
        observation_offsets = [0]*(6*agent_count - 3)

        initial_state_mean = sum([
            [   agent['x0'],
                agent['y0'],
                agent['theta0']]
            for agent in config['agents']],
            [])
        initial_state_covariance = np.zeros((3*agent_count,3*agent_count))

        self.kf = pykalman.KalmanFilter(
            transition_matrices = transition_matrix,
            observation_matrices = observation_matrix,
            transition_covariance = transition_covariance,
            observation_covariance = observation_covariance,
            transition_offsets = transition_offsets,
            observation_offsets = observation_offsets,
            initial_state_mean = initial_state_mean,
            initial_state_covariance = initial_state_covariance,
            random_state = 0
        )

        self.prev_state = initial_state_mean
        self.prev_covariance = initial_state_covariance

    def estimate(self, moves, observations):
        agent_ids = [m.id for m in moves.values()]
        agent_ids.reverse()
        agent_count = len(agent_ids)

        ctrl = np.array(sum([
            [   move.expected_dx,
                move.expected_dy,
                move.expected_dtheta]
            for move in moves.values()],
            []))

        odo = sum([
            [   odo.dx,
                odo.dy,
                odo.dtheta]
            for odo in observations.odometries.values()],
            [])
        odo = sum([
            [   odo[3*i] + self.prev_state[3*i],
                odo[3*i+1] + self.prev_state[3*i+1],
                odo[3*i+2] + self.prev_state[3*i+2]]
            for i in range(agent_count)],
            [])

        poses = sum([
            [   r.dx,
                r.dy,
                r.dtheta]
            for r in list(observations.ranges.values())[1:]],
            [])
        observations.ranges.values()
        obs = np.array(odo + poses)

        (means, covariance) = self.kf.filter_update(
                self.prev_state,
                self.prev_covariance,
                observation = obs,
                transition_offset = ctrl)

        self.prev_state = means
        self.prev_covariance = covariance

        result = dict(
            [   (   agent_ids[i],
                    Estimation(
                        agent_id = agent_ids[i],
                        x = means[3*i],
                        y = means[3*i+1],
                        theta = means[3*i+2]))
                for i in range(agent_count)])

        return result





def _build_observation_matrix(agent_count):
    row = []
    col = []
    data = []

    for i in range(3*agent_count):
        row.append(i)
        col.append(i)
        data.append(1)

    for i in range(agent_count-1):
        row.append(3*(agent_count+i))
        col.append(0)
        data.append(1)

        row.append(3*(agent_count+i) + 1)
        col.append(1)
        data.append(1)

        row.append(3*(agent_count+i) + 2)
        col.append(2)
        data.append(1)

        row.append(3*(agent_count+i))
        col.append(3*(i+1))
        data.append(-1)

        row.append(3*(agent_count+i) + 1)
        col.append(3*(i+1) + 1)
        data.append(-1)

        row.append(3*(agent_count+i) + 2)
        col.append(3*(i+1) + 2)
        data.append(-1)

    return sp.coo_matrix((data, (row, col))).todense()
