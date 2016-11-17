import sys, botpen, os, yaml
import argparse

if __name__ == "__main__":

    argparser = argparse.ArgumentParser(prog = "BotPen")
    argparser.add_argument('-v', action = 'store_true', help='enables the visualizer')
    argparser.add_argument('-o', nargs = 1, help = "the output directory" )
    argparser.add_argument('config_path', help='the path to the configuration file')

    args = argparser.parse_args()

    with open(os.path.abspath(args.config_path)) as f:
        config_doc = f.read()
    config_dom = yaml.load(config_doc)

    config_dom['view_on'] = args.v
    botpen.main(config_dom, args.o)
