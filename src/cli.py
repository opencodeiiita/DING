import argparse
from src import data

def init(args):
    data.init(args.path)

def hash_objects(args):
    data.hash_objects(args.file, args.obj_type)

def cat_file(args):
    data.cat_file(args.hash, args.obj_type)

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

    ## hash-objects
    hash_parser = commands.add_parser("hash-objects", help="hashes and stores the file")
    hash_parser.add_argument("file", help="the file to be hashed")
    hash_parser.add_argument(
        "-t", "--type", 
        dest="obj_type",
        default="blob",
        choices=["blob", "tree", "commit", "tag"],
        help="object type (default: blob)"
    )
    hash_parser.set_defaults(func=hash_objects)

    ## cat-file
    cat_parser = commands.add_parser(
        "cat-file", help="prints out the uncompressed data"
    )
    cat_parser.add_argument(
        "hash", help="the hash (or start of hash) of file to decompress"
    )
    cat_parser.add_argument(
        "-t", "--type",
        dest="obj_type",
        help="specify expected object type"
    )
    cat_parser.set_defaults(func=cat_file)

    return parser.parse_args()


def main():
    args = parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
