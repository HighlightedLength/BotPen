__all__ = [
    'main',
    'bootstrap',
    'AppEngine']

from botpen.__bootstrap import bootstrap
from botpen.app_engine import AppEngine

def main(config, view_on, output_path):
    container = bootstrap(config, view_on, output_path)
    app_engine = container.lookup("AppEngine")

    app_engine.setup()
    app_engine.run()
