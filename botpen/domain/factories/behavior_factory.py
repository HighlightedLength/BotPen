class BehaviorFactory:
    def __init__(self, agent_repo, behavior_resolver):
        self.agent_repo = agent_repo
        self.behavior_resolver = behavior_resolver

    def setup(self, config):
        defaults = config['agent_defaults']
        for agent in config['agents']:
            self.behavior_resolver.setup(agent, defaults)

    def build_updates(self, time):
        result = {}

        agents = self.agent_repo.list()
        for agent in agents:
            result[agent.id] = self.behavior_resolver.build_behavior(agent, time)

        return result
