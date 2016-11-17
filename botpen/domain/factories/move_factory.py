from botpen.domain.models import Move
import math
class MoveFactory:
    def __init__(self, random, agent_repo):
        self.rng = random
        self.agent_repo = agent_repo

    def build_updates(self, behaviors):

        result = {}

        for agent_id in behaviors:
            behavior = behaviors[agent_id]
            agent = self.agent_repo.get(agent_id)

            dx_noise = self.rng.gauss(0, agent.actuation_noise_x)
            dx = behavior.x + dx_noise

            dy_noise = self.rng.gauss(0, agent.actuation_noise_y)
            dy = behavior.y + dy_noise

            dtheta_noise = self.rng.gauss(0, agent.actuation_noise_theta)
            dtheta = behavior.theta + dtheta_noise

            theta = agent.theta + dtheta
            revolutions = math.floor(theta/(2*math.pi))
            theta -= revolutions * 2 * math.pi
            result[agent.id] = Move(
                id = agent_id,
                expected_dx = behavior.x,
                noise_dx = dx_noise,
                actual_dx = dx,
                x = agent.x + dx,

                expected_dy = behavior.y,
                noise_dy = dy_noise,
                actual_dy= dy,
                y = agent.y + dy,

                expected_dtheta = behavior.theta,
                noise_dtheta = dtheta_noise,
                actual_dtheta = dtheta,
                theta = theta)

        return result
