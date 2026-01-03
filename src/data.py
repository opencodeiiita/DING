import os
import hashlib
from compression import zstd  # <--- New Python 3.14 Standard Library import

DING_DIR = ".ding"


def init(path):
    abs_path = os.path.abspath(path)

    if not os.path.exists(abs_path):
        print(f"Error: path does not exist: {abs_path}")
        return

    if not os.path.isdir(abs_path):
        print(f"Error: not a directory: {abs_path}")
        return

    ding_path = os.path.join(abs_path, DING_DIR)
    objects_path = os.path.join(ding_path, "objects")

    if os.path.exists(ding_path):
        print("It is already a ding repository")
        return

    os.mkdir(ding_path)
    os.mkdir(objects_path)
    print(f"Initialisied a ding repo in {ding_path}")


def repo_path():
    cwd = os.getcwd()

    while True:
        ding_path = os.path.join(cwd, DING_DIR)

        if os.path.exists(ding_path):
            return cwd

        parent = os.path.dirname(cwd)
        if parent == cwd:
            break
        cwd = parent

    return None


def hash_objects(args):
    repo = repo_path()
    if repo is None:
        print("error: not inside a ding repository")
        return
    ding_path = os.path.join(repo, DING_DIR)

    objects_path = os.path.join(ding_path, "objects")
    if not os.path.exists(objects_path):
        os.mkdir(objects_path)

    filename = args.file
    try:
        with open(filename, "rb") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"error: file not found: {filename}")
        return

    oid = hashlib.sha256(content).hexdigest()
    print(oid)
    
    # Compress the content using the new zstd std lib module
    compressed_content = zstd.compress(content)
    
    object_file_path = os.path.join(objects_path, oid)
    with open(object_file_path, "wb") as f:
        f.write(compressed_content)