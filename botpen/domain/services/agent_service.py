class AgentService:
    def __init__(self,
            agent_factory,
            behavior_factory,
            move_factory,
            obs_factory,
            estimate_factory,
            agent_repository):
        self.agent_factory = agent_factory
        self.behavior_factory = behavior_factory
        self.move_factory = move_factory
        self.obs_factory = obs_factory
        self.estimate_factory = estimate_factory
        self.agent_repository = agent_repository

    def setup(self, config):
        agents = self.agent_factory.build_new(config)
        for agent in agents:
            self.agent_repository.add(agent)

        behaviors = self.behavior_factory.setup(config)
        self.estimate_factory.setup(config)


    def step(self, time_step):
        behaviors = self.behavior_factory.build_updates(time_step)

        #move the agents
        moves = self.move_factory.build_updates(behaviors)

        #observe the agents
        observations = self.obs_factory.build_updates(moves)

        #estimate the agents
        estimates = self.estimate_factory.build_updates(moves, observations)

        #record changes
        agent_updates = self.agent_factory.build_updates(moves)
        for agent in agent_updates:
            self.agent_repository.update(agent)

        return {
            'time': time_step,
            'agents': agent_updates,
            'observations': observations,
            'estimates': estimates
        }
