import botpen
import argparse, os

def batch():
    argparser = argparse.ArgumentParser(prog = "batchplot")
    argparser.add_argument('directory', help='a format for the output path')
    argparser.add_argument('output_path', help='the output file')

    args = argparser.parse_args()

    logs = os.listdir(args.directory)

    print("output {0}".format(args.output_path))

    for log in logs:
        rel_path = os.path.join(args.directory,log)
        abs_path = os.path.abspath(rel_path)

        print(abs_path)


if __name__ == "__main__":
    batch()
