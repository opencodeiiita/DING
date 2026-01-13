import os
import hashlib
from compression import zstd
import sys


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

def hash_objects(filename, obj_type="blob"):
    """Hash file content with object type prefix (default: blob)"""
    repo = repo_path()
    if repo is None:
        print("error: not a ding repository")
        return

    ding_path = os.path.join(repo, DING_DIR)

    objects_path = os.path.join(ding_path, "objects")
    if not os.path.exists(objects_path):
        os.makedirs(objects_path, exist_ok=True)

    try:
        with open(filename, "rb") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"error: file not found: {filename}")
        return

    # Create header: "type size\x00"
    header = f"{obj_type} {len(content)}\x00".encode('utf-8')
    store_data = header + content
    
    # Hash the header + content (Git style)
    oid = hashlib.sha256(store_data).hexdigest()
    print(oid)

    # Compress and store
    compressed_data = zstd.compress(store_data)
    object_file_path = os.path.join(objects_path, oid)
    with open(object_file_path, "wb") as f:
        f.write(compressed_data)

def cat_file(search_hash, expected_type=None):
    """Print object content if type matches (renamed from decompress)"""
    repo = repo_path()
    if repo is None:
        print("error: not a ding repository")
        return

    ding_path = os.path.join(repo, DING_DIR)
    objects_path = os.path.join(ding_path, "objects")
    if not os.path.exists(objects_path):
        print("error: no objects directory")
        return

    hashes = []
    for entry in os.listdir(objects_path):
        full_path = os.path.join(objects_path, entry)
        if os.path.isfile(full_path):
            hashes.append(entry)

    if len(hashes) < 1:
        print("error: no file has been hashed yet")
        return

    filtered = [h for h in hashes if h.startswith(search_hash)]

    if len(filtered) < 1:
        print(f"error: no hash matches the search-hash: {search_hash}")
        return

    if len(filtered) > 1:
        print("Multiple files found:")
        for h in filtered:
            print(f"- {h}")
        return

    hash_oid = filtered[0]
    print(f"Selected hash: {hash_oid}\n")

    full_path = os.path.join(objects_path, hash_oid)
    with zstd.open(full_path, "rb") as f:
        decompressed = f.read()

    # Parse header: find null byte separator
    try:
        null_pos = decompressed.index(b'\x00')
        header = decompressed[:null_pos].decode('utf-8')
        content = decompressed[null_pos + 1:]
        
        # Extract type from header
        obj_type = header.split()[0]
        
        # Verify expected type if provided
        if expected_type and obj_type != expected_type:
            print(f"error: expected type '{expected_type}', got '{obj_type}'")
            return
        
        # Output content
        sys.stdout.buffer.write(content)
        return
        
    except ValueError:
        print("error: invalid object format (no null byte found)")
    except Exception as e:
        print(f"error: {e}")
