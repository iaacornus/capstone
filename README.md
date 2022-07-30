![](https://api.codiga.io/project/33619/score/svg)

# Capstone

This branch is for implementation of Python > 3.10 features.

This is program, with experimental and some untested parts, starting from commit by iaacornus: 7d8829659ae63ca88bca17d200d3fc3cfff327de, for example of implementation and use of the project of Group 5 for fulfillment in subject, Capstone.

# Install

Refer to [install](INSTALL.md) for more detailed instructions on how to install the program.

## Simple install

Clone the repository with:

```bash
git clone https://github.com/testno0/capstone
```

Execute the setup script, which includes user setup with:

```bash
./capstone/src/sutils/./pre_setup.sh
```

# EasyWiz

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
