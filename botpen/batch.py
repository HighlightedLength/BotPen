import botpen
import argparse

def batch():
    argparser = argparse.ArgumentParser(prog = "BotPen")
    argparser.add_argument('-v', action = 'store_true', help='enables the visualizer')
    argparser.add_argument('iterations', help='the number of iterations to run', type = int)
    argparser.add_argument('output_path_format', help='a format for the output path')
    argparser.add_argument('config_path', help='the path to the configuration file')

    args = argparser.parse_args()

    path_format = args.output_path_format

    for i in range(args.iterations):
        path = path_format.format(i + 1)
        print('on job {0} out of {1}'.format(i + 1 ,args.iterations))
        print('outputting to {0}'.format(path))
        botpen.main(args.config_path, args.v, path)
        print('done')

if __name__ == "__main__":
    batch()
