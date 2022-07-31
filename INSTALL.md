# Installation

You can either do this or run `install.sh`.

Clone the repository with `git`, if `git` is not installed install it via the package manager.

```bash
git clone --branch vEx https://github.com/testno0/capstone
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
+-- archive
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
+-- install.sh
+-- LICENSE
+-- pre_setup.sh
+-- README.md
+-- requirements.txt
+-- sample
|   +-- test_1.png
|   +-- test_2.png
|   +-- test_3.png
|   +-- test_4.png
|   `-- test_5.png
+-- src
|   +-- cli.py
|   +-- demo.py
|   +-- __init__.py
|   +-- main.py
|   +-- misc
|   |   +-- __init__.py
|   |   +-- msg
|   |   |   +-- alert.msg
|   |   |   +-- intruder.msg
|   |   |   +-- setup.msg
|   |   |   `-- student.msg
|   |   `-- signs.py
|   +-- sutils
|   |   +-- __init__.py
|   |   +-- password_gen.py
|   |   `-- update.py
|   `-- utils
|       +-- access.py
|       +-- code_email.py
|       +-- face_recog.py
|       +-- function.py
|       `-- __init__.py
+-- src_rfid_locker
|   +-- include
|   |   `-- README
|   +-- platformio.ini
|   +-- src
|   |   `-- main.cpp
|   `-- test
|       `-- README
`-- user_setup.sh
```

Then move the source code of the program from the package directory, with `cp -r src/* $HOME/.easywiz/`. And add `alias easywiz="python $HOME/.easywiz/cli.py` before `unset rc`, or move `.bashrc` to `$HOME/` and do `source $HOME/.bashrc`.

For user setup, create a file named `user_info` in `$HOME/.easywiz/` and include your email, username, password hash using SHA256, and school name, in each new line. For password, you can use `python $HOME/.easywiz/sutils/password_gen.py` to generate a password, or use your own.

And finally, reboot.
