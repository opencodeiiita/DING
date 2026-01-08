import argparse
from src import data

def init(args):
    data.init(args.path)


def hash_objects(args):
    data.hash_objects(args.file)


def decompress(args):
    data.decompress(args.hash)


def parse_args():
    parser = argparse.ArgumentParser(prog="ding")

    # COMMANDS
    commands = parser.add_subparsers(dest="command", required=True)

    ## init
    init_parser = commands.add_parser(
        "init", help="initializes an empty ding repository"
    )
    init_parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="directory to initialize the ding repository in (default: current directory)",
    )
    init_parser.set_defaults(func=init)

    ## hash
    hash_parser = commands.add_parser("hash", help="hashes and stores the file")
    hash_parser.add_argument(
        "file", help="the file to be hashed"
    )
    hash_parser.set_defaults(func=hash_objects)

    ## cat-file
    hash_parser = commands.add_parser("cat-file", help="prints out the uncompressed data")
    hash_parser.add_argument(
        "hash", help="the hash (or start of hash) of file to decompress"
    )
    hash_parser.set_defaults(func=decompress)

    return parser.parse_args()


def main():
    print("Ding Dong, who's there?\n"
          "— Open Source\n"
          "Open Source who?\n"
          "Free to use, pay with your time.\n")
    args = parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
