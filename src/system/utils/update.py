from os import system
from os.path import expanduser, exists

from rich.console import Console

from src.bin.access import access


def update():
    HOME = expanduser("~")
    console = Console()
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
        else:
            console.log(
                "[bold magenta][+] Pulling updates ...[/bold magenta]"
            )
            system(f"cd {HOME}/.att_sys/repo/ && git pull")


if __name__ == "__main__":
    update()
