from os import system
from os.path import expanduser, exists

from rich.console import Console

from src.utils.access import access
from src.misc.signs import Signs


def update() -> None:
    """For fetching update of the repository."""

    console: object = Console()
    HOME: str = expanduser("~")
    access(HOME)

    with console.status(f"{Signs.PROC} Updating repository ..."):
        if not exists(f"{HOME}/repo"):
            print(
                (
                    f"{Signs.RFAIL} Local repository not found.\n"
                    f"{Signs.RPROC} Cloning the repository ..."
                )
            )

            # clone the repository and redirect stdout to /dev/null, this is a secret
            system(
                (
                    f"git clone --branch database https://github"
                    ".com/testno0/capstone {HOME} &> /dev/null"
                )
            )
            system("mv $HOME/capstone $HOME/.easywiz/repo/")
        else:
            print(f"{Signs.RPROC} Pulling updates ...")
            system(f"cd {HOME}/.easywiz/repo/; git pull > /dev/null")


if __name__ == "__main__":
    update()
