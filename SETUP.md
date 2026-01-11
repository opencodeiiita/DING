# SETUP Guide for DING 🚀

_A learning-first Version Control System built from scratch._  
Get it running in **under 5 minutes**. No stress, no fluff.

---

## ⚡ TL;DR (Speedrun)

    git clone https://github.com/opencodeiiita/DING.git
    cd DING
    python -m venv venv
    # Windows: venv\Scripts\activate
    # macOS/Linux: source venv/bin/activate
    pip install -e .
    ding --help

If that worked — you’re done ✅

---

## 📦 Prerequisites

Make sure you have:

- **Python 3.10 or higher**
  
      python --version

- **pip** (comes with Python)
- **Git** (for cloning the repository)

💡 Tip:  
If you have multiple Python versions installed, prefer:

    python3 -m venv venv

---

## 🔧 Installation

### 1️⃣ Clone the Repository

    git clone https://github.com/opencodeiiita/DING.git
    cd DING

---

### 2️⃣ Create & Activate a Virtual Environment (Recommended)

Using a virtual environment keeps DING isolated from your global Python setup.

**Windows**

    python -m venv venv
    venv\Scripts\activate

**macOS / Linux**

    python3 -m venv venv
    source venv/bin/activate

You should now see `(venv)` at the start of your terminal.

---

### 3️⃣ Install DING (Editable Mode)

    pip install -e .

The `-e` flag installs DING in editable mode, so changes to the source code apply immediately.

---

## ✅ Verify Installation

    ding --help

Expected output:

    usage: ding [-h] {init,hash,cat-file} ...

    positional arguments:
      {init,hash,cat-file}
        init        initialize an empty ding repository
        hash        hash and store a file
        cat-file    read stored object content

If you see this, DING is installed correctly 🎉

---

## 🎮 Quick Start

### Initialize a DING Repository

    mkdir my-project
    cd my-project
    ding init

This creates a `.ding/` directory for internal storage.

---

## ♻️ Reset a DING Repository

    rm -rf .ding
    ding init


### Hash a File

    echo "DING is actually fire" > test.txt
    ding hash test.txt

Example output:

    abc123def456...

---

### Read Stored Content

    ding cat-file abc123

This decompresses and prints the stored file content.

---

## 🧠 What’s Happening Internally?

- `ding init` creates the `.ding/` directory
- `ding hash`:
  - Reads file content
  - Compresses it
  - Generates a SHA-1 hash
  - Stores it in `.ding/objects/`
- `ding cat-file` retrieves and decompresses stored data

These are the core building blocks of version control systems like Git.

---

## 🚨 Troubleshooting

### `ding: command not found`

Cause: Virtual environment not activated.

Fix:

    # Windows
    venv\Scripts\activate

    # macOS/Linux
    source venv/bin/activate

    pip install -e .

---

### `ModuleNotFoundError`

Cause: Running commands outside the project root.

Fix:

    cd DING
    ding --help

---

### `pip install -e .` fails

Fix:

    pip install --upgrade pip setuptools wheel
    pip install -e .

---

## 📂 Project Structure

    DING/
    ├── setup.py
    ├── README.md
    ├── SETUP.md
    ├── CONTRIBUTING.md
    └── src/
        ├── cli.py
        ├── data.py
        └── base.py

---

## 🎯 Next Steps

- Read `README.md`
- Explore `src/data.py`
- Hash multiple files and compare hashes
- Modify files and observe changes

---


## 🔍 DING vs Git (Mental Model)

| Concept | Git | DING |
|------|-----|------|
| Repo folder | .git | .ding |
| Hashing | SHA-1 | SHA-1 |
| Objects | blobs, trees, commits | objects |
| Goal | Production VCS | Learning internals |

## 📌 Supported Commands

- ding init
- ding hash <file>
- ding cat-file <hash>

## 🧪 Try This Experiment

    echo "hello" > a.txt
    ding hash a.txt

    echo "hello" > b.txt
    ding hash b.txt

Same content → same hash.

## 🧹 Uninstall DING

    pip uninstall ding


## 🎉 You’re Ready

You’ve successfully set up DING and explored how version control works internally.

Now go experiment, break things, and learn for real. 🔥
