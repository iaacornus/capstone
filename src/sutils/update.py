from os import system
from os.path import expanduser, exists

from rich.console import Console

from src.utils.access import access


def update() -> None:
    """For fetching update of the repository."""

    console: object = Console()
    HOME: str = expanduser("~")
    access(HOME)

    with console.status("[bold]> Updating repository ...[/bold]."):
        if not exists(f"{HOME}/repo"):
            console.log(
                "[bold red][-] Local repository not found[/bold red]"
            )
            console.log(
                "[bold magenta][+] Cloning the repository.[/bold magenta]"
            )

            # clone the repository and redirect stdout to /dev/null, this is a secret
            system(
                (
                    f"git clone -b database https://github"
                    ".com/testno0/capstone {HOME} &> /dev/null"
                )
            )
            system("mv $HOME/capstone $HOME/.easywiz/repo/")
        else:
            console.log(
                "[bold magenta][+] Pulling updates ...[/bold magenta]"
            )
            system(f"cd {HOME}/.easywiz/repo/; git pull > /dev/null")


if __name__ == "__main__":
    update()
