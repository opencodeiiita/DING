# Setup for Ding

**Ding is Git's evil twin written in python.**

## To use Ding and enter Agartha:
You should have:
- Python 3.14+
- pip
- Git (to clone the repo)

## Setup
```bash
git clone https://github.com/opencodeiiita/DING.git <br>
cd DING
```

### To Setup a Virtual Environment
```bash
python -m venv venv
```

#### Windows
```shell
venv\Scripts\activate
pip install -e .
```

#### macOS/Linux
```shell
source venv/bin/activate
pip install -e .
```

To run it again anytime after the initial setup, just activate the venv

## Confirmation
If at the end you see
Successfully installed ding-1.0

run `ding -h` to see more instructions
```bash
 > ding -h
usage: ding [-h] {init,hash-objects,cat-file} ...

positional arguments:
  {init,hash-objects,cat-file}
    init                initializes an empty ding repository
    hash-objects        hashes and stores the file
    cat-file            prints out the uncompressed data

options:
  -h, --help            show this help message and exit
```

This means you are good to go

__All done in 67 seconds ✧｡٩(ˊᗜˋ )و✧*｡.__
