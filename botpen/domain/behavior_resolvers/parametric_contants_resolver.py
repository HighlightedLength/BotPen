from domain.models import ParametricBehavior, Control
from util import elf
class ParametricConstantsResolver:
    def __init__(self, parametric_behavior_repo):
        self.parametric_behavior_repo = parametric_behavior_repo

    def is_applicable(self, behavior_type):
        return behavior_type == "ParametricConstants"

    def setup(self, agent, defaults):
        behavior_config = elf.get_default('behavior_config', agent, defaults)

        for behavior in behavior_config:
            self.parametric_behavior_repo.add_behavior(
                agent['id'],
                ParametricBehavior(
                    behavior['time'],
                    behavior['x'],
                    behavior['y'],
                    behavior['theta']
                )
            )

    def build_behavior(self, agent, time):
        behavior = self.parametric_behavior_repo.get(agent.id, time)
        return Control(behavior.x, behavior.y, behavior.theta)
