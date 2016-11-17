from botpen.domain.models import Agent
from botpen.util import elf
class AgentFactory:
    def __init__(self, agent_repo):
        self.agent_repo = agent_repo

    def build_new(self, config):
        defaults = config['agent_defaults']
        agents = config['agents']

        result = [
            Agent(
                id = agent['id'],

                x = elf.get_default('x0', agent, defaults),
                y = elf.get_default('y0', agent, defaults),
                theta = elf.get_default('theta0', agent, defaults),

                actuation_noise_x = elf.get_default('actuation_noise_x', agent, defaults),
                actuation_noise_y = elf.get_default('actuation_noise_y', agent, defaults),
                actuation_noise_theta = elf.get_default('actuation_noise_theta', agent, defaults),

                observation_noise_x = elf.get_default('observation_noise_x', agent, defaults),
                observation_noise_y = elf.get_default('observation_noise_y', agent, defaults),
                observation_noise_theta = elf.get_default('observation_noise_theta', agent, defaults),

                behavior_type = elf.get_default('behavior_type', agent, defaults),
                behavior_config = elf.get_default('behavior_config', agent, defaults)
            )
            for agent in agents
        ]

        return result

    def build_updates(self,moves):
        result = []
        for agent_id in moves:
            move = moves[agent_id]
            agent = self.agent_repo.get(agent_id)

            result.append(
                Agent(
                    id = move.id,

                    x = move.x,
                    y = move.y,
                    theta = move.theta,

                    actuation_noise_x = agent.actuation_noise_x,
                    actuation_noise_y = agent.actuation_noise_y,
                    actuation_noise_theta = agent.actuation_noise_theta,

                    observation_noise_x = agent.observation_noise_x,
                    observation_noise_y = agent.observation_noise_y,
                    observation_noise_theta = agent.observation_noise_theta,

                    behavior_type = agent.behavior_type,
                    behavior_config = agent.behavior_config
                )
            )
        return result
