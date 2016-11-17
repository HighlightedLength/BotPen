class Controller:
    def __init__(self, agent_service, world_service, logger):
        self.agent_service = agent_service
        self.world_service = world_service
        self.logger = logger

    def setup(self, config):
        agents = self.agent_service.setup(config)
        self.world_service.setup(config)

    def step(self):
        time = self.world_service.step()

        results = self.agent_service.step(time)
        #self.logger.info(pformat(results))

        return results

    def process_inputs(self, inputs):
        return self.world_service.update_lifecycle(inputs)

    def get_lifecycle(self):
        return self.world_service.get_lifecycle()
