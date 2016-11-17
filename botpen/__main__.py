import botpen
import argparse

if __name__ == "__main__":

    argparser = argparse.ArgumentParser(prog = "BotPen")
    argparser.add_argument('-v', action = 'store_true', help='enables the visualizer')
    argparser.add_argument('-o', nargs = '?', help = "the output directory" )
    argparser.add_argument('config_path', help='the path to the configuration file')

    args = argparser.parse_args()

    botpen.main(args.config_path, args.v, args.o)
