from domain.models import Control
from util import elf

class DecidingResolver:
    def __init__(self, *resolvers):
        self.resolvers = list(resolvers)

    def setup(self, agent, defaults):
        behavior_type = elf.get_default('behavior_type', agent, defaults)
        behavior_config = elf.get_default('behavior_config', agent, defaults)

        resolver = (
            next(   (   x for x in self.resolvers
                        if x.is_applicable(behavior_type)
                    ),None  )   )
        resolver.setup(agent, defaults)

    def build_behavior(self, agent, time):
        resolver = (
            next(   (   x for x in self.resolvers
                        if x.is_applicable(agent.behavior_type)
                    ),None  )   )
        if resolver:
            return resolver.build_behavior(agent, time)
        else:
            return Control(0,0,0)
