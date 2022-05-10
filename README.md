# Capstone

Development branch of arduino and RFID software, next merge is devel -> v 1.0

# Devel

The merging would be `cli` -> `v1-test-beta` -> `v1`. On May 10, 2022@17:07:56, `face_recog` branch was merged into `devel` branch for further development.

The next merging would be `devel` -> `v1-test-beta`. Some features are optimization of the face recognition algorithm as well as optimization and improvement of other code base.

And finally, `v1-test-beta` would be merged with `v1` for final implementation, marking the start of phase 3.

# Merging

The `devel` as forked into `pep8-adaptation` branch to change the code into PEP 8 guidelines, which will be forked into `pep8-ch-test`, for testing of the changes, and then merged into `devel` branch again for:

> The next merging would be `devel` -> `v1-test-beta`. Some features are optimization of the face recognition algorithm as well as optimization and improvement of other code base.
> And finally, `v1-test-beta` would be merged with `v1` for final implementation, marking the start of phase 3.

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

Starting at:

```bash
commit 08728ed3d6af99f7886b8fdae556b8e3ad18f553
Author: iaacornus <iaacornus.devel@gmail.com>
Date:   Tue May 10 15:17:52 2022 +0800

    add av_cam function to simplify face_recognition.py
```

The whole code undergone again intensive revision to fix all the errors, and improve the whole code base.

# Coding Style

Use [PEP 8](https://peps.python.org/pep-0008/) coding style. A few modifications are made, however, first is instead of 79 characters line limit, 99 is used instead, while the code and docstring limit stays at 72 characters. There is always extra indentation in continuation lines:

```python
# Add some extra indentation on the conditional continuation line.
if (this_is_one_thing
        and that_is_another_thing):
    do_something()

# not this one
if (this_is_one_thing and
    that_is_another_thing):
    do_something()
```

And in closing brackets, do:

```python
# this is suggested
my_list = [
    1, 2, 3,
    4, 5, 6,
    ]

# not this one
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)
```

CamelCase is used in `class` names, and lowercase with underscores or simply lowercase for use in `function` names and variable names.

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
