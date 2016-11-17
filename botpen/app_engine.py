#import botpen.bootstrap
import botpen
import sys

class AppEngine:

    def __init__(self, config, controller, renderer):
        self.config = config
        self.controller = controller
        self.renderer = renderer

    def setup(self):
        self.controller.setup(self.config)

        if self.renderer:
            self.renderer.setup(self.config)

    def run(self):
        finish = False
        proceed = True
        inputs = None

        while not finish:
            if proceed:
                view = self.controller.step()
                if self.renderer:
                    self.renderer.display(view)

            if self.renderer:
                inputs = self.renderer.get_events()

            self.controller.process_inputs(inputs)
            inputs = None

            lifecycle = self.controller.get_lifecycle()
            finish = lifecycle.finish
            proceed = lifecycle.proceed

        if self.renderer:
            self.renderer.close()
        sys.exit()
