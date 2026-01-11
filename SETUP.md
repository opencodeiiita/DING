# SETUP.md  
## DING — Ding Is Not Git

This guide explains how to set up **DING** locally and start using it in **under 5 minutes**.

No frameworks.  
No external dependencies.  
Just **Python**.

---

## 1. Prerequisites

You only need:

- **Python 3.8 or higher**
- **pip** (comes with Python)

Verify installation:

```bash
python3 --version
pip --version

If both commands work, you’re ready.

----

## 2. Clone the Repository

git clone https://github.com/opencodeiiita/DING.git
cd DING

⚠️ Git is used only to download DING.
DING itself is not Git.

----

## 3. Install DING

From the project root, 

Run:
pip install -e .

This will:
	- Install ding as a CLI command
	- Link the command directly to the source code
	- Allow instant testing while developing 

----

## 4. Verify Installation

Run:
ding --help

If you see a help message, ✅ DING is installed correctly.

----

## 5. Create Your First DING Repository

Create a test directory:
mkdir test-ding
cd test-ding

Initialize DING:
ding init

This creates DING’s internal metadata directory (similar to .git, but for DING).

----

## 6. Basic Usage (Quick Start)

echo "hello ding" > file.txt
ding status
ding commit -m "first commit"
ding log

You’ve just used a version control system built from scratch.

----

## 7. Project Structure

DING/
├── setup.py        # Package & CLI configuration
├── README.md
└── src/
    ├── cli.py      # Entry point for `ding` command
    ├── base.py     # Core VCS logic
    ├── data.py     # Object storage
    └── diff.py     # Diff & status logic

The ding command maps directly to src/cli.py.

----

## 8. Common Problems & Fixes

❌ ding: command not found

Run again from project root:
pip install -e .

If needed:
python3 -m pip install -e .

❌ Python version too old

Ensure Python ≥ 3.8:
python3 --version

----

## 9. Want to Contribute?

Before contributing:
	- Read README.md
	- Read CONTRIBUTING.md
	- Follow branch naming and PR format strictly

Invalid PRs will not be accepted.

✅ Setup Complete
You’re done 🎉
	- DING installed
	- CLI working
	- Repository initialized

----


