from botpen.domain.models import Range, Odometry, Observation
from util import elf

class ObservationFactory:
    def __init__(self, rng, agent_repo):
        self.rng = rng = rng
        self.agent_repo = agent_repo

    def build_updates(self, moves):

        odometries = {}
        ranges = {}

        base_agent = next (iter (moves.values()))

        for agent_id in moves:
            move = moves[agent_id]
            agent = self.agent_repo.get(agent_id)

            x_noise = self.rng.gauss(0, agent.observation_noise_x)
            dx = move.actual_dx + x_noise

            y_noise = self.rng.gauss(0, agent.observation_noise_y)
            dy = move.actual_dy + y_noise

            theta_noise = self.rng.gauss(0, agent.actuation_noise_theta)
            dtheta = elf.normalize_radians(move.actual_dtheta + theta_noise)

            odometries[agent.id] = Odometry(
                noise_dx = x_noise,
                dx = dx,

                noise_dy = y_noise,
                dy = dy,

                noise_dtheta = theta_noise,
                dtheta = dtheta)

            ranges[agent.id] = Range(
                dx = move.x - base_agent.x,
                dy = move.y - base_agent.y,
                dtheta = move.theta - base_agent.theta)

        return Observation(
            odometries = odometries,
            ranges = ranges,
            base_agent = base_agent.id
        )
