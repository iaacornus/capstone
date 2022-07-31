# Capstone

![](https://api.codiga.io/project/34257/score/svg)

Production branch of the project but with unoptimized and stupid code.

# Install

## Advanced install

Refer to [install](INSTALL.md) for instructions on how to install the program.

## Simple install

Clone the repository with:

```bash
git clone https://github.com/testno0/capstone
```

Install dependencies with

```bash
pip install -r requirements.txt
```

Activate the `virtual env` from python using this tutorial [https://realpython.com/python-virtual-environments-a-primer/](https://realpython.com/python-virtual-environments-a-primer/).

# TapTap

The help can be accessed with `-h` flag and outputs all the help.

```bash
usage: taptap [OPTIONS]

This is a program designed to interact with the TapTap, an RFID system designed by Capstone Group 5.

options:
  -h, --help           show this help message and exit
  -use, --use          Use the system.
  -update, --update    Update the system
  -setup, --usersetup  Setup the user (prompts to input the passphrase sent via email, if used again).
  -destroy, --destroy  Destroy the user database.
  -demo, --demo        Face recognition demonstration.
  -v, --verbose        Show the processes of program.
```
