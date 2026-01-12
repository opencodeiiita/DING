# Setup for Ding

**Ding is Git's evil twin written in python.**

## To use Ding and enter Agartha:
You should have:
- **Python 3.14+** installed
- **pip** (Python package manager)
- **Git** (for cloning the repository)

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/opencodeiiita/DING.git
cd DING
```

### 2. Set Up a Virtual Environment
A virtual environment keeps your dependencies isolated and prevents conflicts.
```bash
python -m venv venv
```

### 3. Activate the Environment & Install Ding

**Windows:**
```powershell
venv\Scripts\activate
pip install -e .
```

**macOS/Linux:**
```bash
source venv/bin/activate
pip install -e .
```

Once activated, you'll see `(venv)` prefixed in your terminal prompt.

## Verify Installation

After installation, you should see:
```bash
Successfully installed ding-1.0
```

Test that Ding is working by running:
```bash
ding -h
```

**Expected output:**
```bash
usage: ding [-h] {init,hash-objects,cat-file} ...

positional arguments:
  {init,hash-objects,cat-file}
    init                initializes an empty ding repository
    hash-objects        hashes and stores the file
    cat-file            prints out the uncompressed data

options:
  -h, --help            show this help message and exit
```

## Usage Tips

**Reactivating the environment:** The next time you want to use Ding, simply activate the virtual environment:
- **Windows:** `venv\Scripts\activate`
- **macOS/Linux:** `source venv/bin/activate`


This means you are good to go

## Troubleshooting

### `ding: command not found`
This usually means either:
1. The virtual environment isn't activated
2. The installation didn't complete properly

**Solution:**
```bash
# Make sure you're in the DING directory
cd DING

# Activate the virtual environment
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows

# Reinstall
pip install -e .
```

---

__All done in 71 seconds ✧｡٩(ˊᗜˋ )و✧*｡.__
