class EstimationRepo:
    def __init__(self):
        self.estimations = {}

    def get(self, agent_id):
        return self.estimations[agent_id]

    def update(self, estimation):
        self.estimations[estimation.agent_id] = estimation
