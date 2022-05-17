# Installation

You can either do this or run `pre_setup.sh` and `user_setup.sh`.

Clone the repository with `git`, if `git` is not installed install it via the package manager.

```bash
git clone --branch v1.0 https://github.com/testno0/capstone
```

Or you can download the latest source code from github.

Install the dependencies, since this tutorial assumes that the Linux distribution being used is Fedora Linux, the command is:

```bash
sudo dnf install python3-dlib cmake python3-pip
python -m pip install pip --upgrade
pip install -r requirements.txt
```

The package layout of the program is:

```
$HOME/
`--.att_sys/
|  `--bin/
|  |  `--access.py
|  |  `--code_email.py
|  `--system/
|  |  `--utils/
|  |  |  `--password_gen.py
|  |  |  `--update.py
|  |  `--.bashrc
|  |  `--pre_setup.sh
|  |  `--user_setup.sh
|  `--misc
|  |  `--colors.py
|  `--cli.py
|  `--main.py
|  `--function.py
|  `--face_recog.py
|  `--demo.py
`--...
```

Then move the source code of the program from the package directory, via `cp -r src/* $HOME/.att_sys/`. And add `alias taptap="python $HOME/.att_sys/cli.py` before `unset rc`, or move `.bashrc` to `$HOME/` and do `source $HOME/.bashrc`.

For user setup, create a file named `user_info` in `$HOME/.att_sys/` and include your email, username, password, and school name, in each new line. For password, you can use `python $HOME/.att_sys/system/utils/password_gen.py` to generate a password, or use your own.

And finally, reboot.
