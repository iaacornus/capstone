# Capstone

Development branch of arduino and RFID software, next merge is devel -> v 1.0

# Devel

The merging would be `cli` -> `v1-test-beta` -> `v1`

# Install

Clone the repository with

```bash
git clone --branch cli https://github.com/testno0/capstone
```

Install dependencies with

```bash
pip install -r requirements.txt
```

Activate the `virtual env` from python using this tutorial [https://realpython.com/python-virtual-environments-a-primer/](https://realpython.com/python-virtual-environments-a-primer/).

# Notes
Starting at:

```bash
commit 64c669b4297b434e6f474a4f7909dce9df4d2a79
Author: testno0 <jaaaderang@gmail.com>
Date:   Thu Apr 28 19:43:02 2022 +0800

    improved syntaxes and formatting
```

The whole code undergone intensive revision to fix all the errors, and improve the whole code base, marking the start of phase 2.

# TapTap

The help can be accessed with `-h` flag and outputs all the help.

```
python cli.py -h -> taptap -h
usage: taptap [OPTIONS]

This is a program designed to interact with the TapTap, an RFID system
designed by Capstone Group 5.

options:
  -h, --help     show this help message and exit
  -U, --update   Update the system
  -s, --setup    Setup the system (again -- prompts to input the passphrase
                 sent via email, if used again).
  -d, --destroy  Destroy the user database.
```