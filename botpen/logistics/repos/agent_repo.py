class AgentRepo:
    def __init__(self):
        self.agents = {}

    def add(self, agent):
        if not agent.id in self.agents:
            self.agents[agent.id] = agent
        else:
            raise KeyError("agent {0} already exists".format(agent.id))

    def get(self, id):
        return self.agents.get(id)

    def update(self, agent):
        if not agent.id in self.agents:
            raise KeyError("agent {0} does not exist".format(agent.id))
        else:
            self.agents[agent.id] = agent

    def delete(self, id):
        del self.agents[agent.id]

    def list(self):
        return self.agents.values()

    def count(self):
        return len(self.agents)
