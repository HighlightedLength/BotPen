__all__ = [
    'main',
    'bootstrap',
    'AppEngine',
    'batch']

from botpen.__bootstrap import bootstrap
from botpen.app_engine import AppEngine
import sys, os, yaml

def main(config_path, view_on, output_path):
    with open(os.path.abspath(config_path)) as f:
        config_doc = f.read()

    config = yaml.load(config_doc)
    config['view_on'] = view_on



    if output_path:
        config['output_path'] = output_path
        print(config['output_path'])
    container = bootstrap(config)
    app_engine = container.lookup("AppEngine")

    app_engine.setup()
    app_engine.run()
