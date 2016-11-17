__all__ = [
    'main',
    'bootstrap',
    'AppEngine',
    'batch']

from botpen.__bootstrap import bootstrap
from botpen.app_engine import AppEngine

def main(config, output_path):
    if output_path:
        config['output_path'] = output_path[0]
    container = bootstrap(config, output_path)
    app_engine = container.lookup("AppEngine")

    app_engine.setup()
    app_engine.run()
