# Installation

You can either do this or run `pre_setup.sh` and `user_setup.sh`.

Clone the repository with `git`, if `git` is not installed install it via the package manager.

```bash
git clone --branch v1.f https://github.com/testno0/capstone
```

Or you can download the latest source code from github.

Install the dependencies, since this tutorial assumes that the Linux distribution being used is Fedora Linux, the command is:

```bash
sudo dnf install python3-dlib cmake python3-pip
python -m pip install pip --upgrade
pip install -r requirements.txt
```

## Project layout

```
+-- archives
|   +-- README.md
|   +-- rfid
|   |   +-- main2.cpp
|   |   +-- main.cpp
|   |   `-- main.cpp.bak
|   `-- test_faces
|       +-- biden1.jpg
|       +-- biden2.jpg
|       +-- f0.jpg
|       +-- f1.jpg
|       +-- f2.jpg
|       +-- f3.jpg
|       +-- f4.jpg
|       +-- f5.jpg
|       +-- f6.jpg
|       +-- f7.jpg
|       +-- f8.jpg
|       +-- f9.jpg
|       +-- obama1.jpg
|       `-- obama2.jpg
+-- INSTALL.md
+-- LICENSE
+-- README.md
+-- requirements.txt
+-- rfid_locker
|   +-- include
|   |   `-- README
|   +-- platformio.ini
|   +-- src
|   |   `-- main.cpp
|   `-- test
|       `-- README
+-- sample
|   +-- test_1.png
|   +-- test_2.jpg
|   +-- test_2.png
|   +-- test_3.png
|   +-- test_4.png
|   `-- test_5.png
`-- src
    +-- bin
    |   +-- access.py
    |   `-- code_email.py
    +-- cli.py
    +-- demo.py
    +-- face_recog.py
    +-- function.py
    +-- __init__.py
    +-- main.py
    +-- misc
    |   +-- colors.py
    |   `-- __init__.py
    `-- system
        +-- __init__.py
        +-- pre_setup.sh
        +-- user_setup.sh
        `-- utils
            +-- __init__.py
            +-- password_gen.py
            `-- update.py
```

Then move the source code of the program from the package directory, via `cp -r src/* $HOME/.att_sys/`. And add `alias taptap="python $HOME/.att_sys/cli.py` before `unset rc`, or move `.bashrc` to `$HOME/` and do `source $HOME/.bashrc`.

For user setup, create a file named `user_info` in `$HOME/.att_sys/` and include your email, username, password, and school name, in each new line. For password, you can use `python $HOME/.att_sys/system/utils/password_gen.py` to generate a password, or use your own.

And finally, reboot.
