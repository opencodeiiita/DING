import time
import zlib
import gzip
import lzma
import zstandard as zstd
from pathlib import Path


# Load test file (we are already inside src/)
data = Path("cli.py").read_bytes()


def test(name, compress_fn):
    start = time.time()
    compressed = compress_fn(data)
    duration = time.time() - start
    return name, len(compressed), duration


results = [
    test("zlib", lambda d: zlib.compress(d, 6)),
    test("gzip", lambda d: gzip.compress(d, 6)),
    test("lzma", lambda d: lzma.compress(d)),
]

# Zstandard compression
cctx = zstd.ZstdCompressor(level=3)
start = time.time()
zstd_compressed = cctx.compress(data)
zstd_time = time.time() - start
results.append(("zstd", len(zstd_compressed), zstd_time))


# Print results
print("\nCompression Benchmark Results\n" + "-" * 40)
for name, size, t in results:
    print(f"{name:<6} | size: {size:6} bytes | time: {t:.6f}s")
