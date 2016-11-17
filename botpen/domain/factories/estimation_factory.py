class EstimationFactory:
    def __init__(self,  *args):
        self.estimators  = list(args)

    def setup(self, config):
        for estimator in self.estimators:
            estimator.setup(config)

    def build_updates(self, moves, odometries):
        result = {}
        for estimator in self.estimators:
            estimations = estimator.estimate(moves, odometries)
            result[estimator.name] = estimations

        return result
