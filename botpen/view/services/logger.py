class Logger:
    config = None

    def setup(self, config):
        self.config = config

    def log(self, view):
        output_path = self.config.get("output_path")
        print("in logger: {0}".format(output_path))
