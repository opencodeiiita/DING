# DING — Ding Is Not Git

_A complete Version Control System built from scratch in Python._

**DING** is an version control system developed as part of **OpenCode by IIITA**.  
The goal of this project is to build a VCS that implements **most of the features** git

DING focuses on teaching core concepts such as content-addressable storage, snapshots, commits, branching, diffs, and logs - all through readable, well-structured Python code.

If you've ever wondered _“What actually happens when I run `git commit`?”_, DING is for you.

---

## Objectives

- Build a **fully functional VCS**, not a mock or toy model
- Keep the implementation **simple, readable, and hackable**
- Encourage contributors to **learn by building**, not just using tools

---

## Features

### Repository Initialization

- Initialize a DING repository inside any directory
- Creates internal metadata and object storage
- Inspired by Git’s `.git` structure

### Object Storage

- Content-addressable storage using hashes
- Stores:
  - Blobs (file contents)
  - Trees (directory snapshots)
  - Commits (project states)

### Commits & History

- Snapshot-based commits
- Commit metadata (message, parent, timestamp)
- Linear history traversal
- Commit logs similar to `git log`

### Branching

- Lightweight branch references
- HEAD pointer management
- Switch between branches safely

### Diff & Status

- Show changes between commits
- Working directory vs last commit
- Track modified, added, and deleted files

---

## Getting Started

Before starting - check out our [CONTRIBUTING.md](https://github.com/opencodeiiita/DING/blob/main/CONTRIBUTING.md) to get a refresher on contribution and general workflow.

---

## Tech Stack

### **Language**

- **Python 3.x**

### **External Dependencies**

_NONE, build from scratch just using std_

---

## Project Structure

```
.
├── setup.py
└── ugit
    ├── base.py
    ├── cli.py
    ├── data.py
    ├── diff.py
    └── remote.py
```

---

## Setup
Check Out the SetUp Guide [here](./Setup.md)
