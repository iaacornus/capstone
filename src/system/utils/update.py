import sys
import os

from rich.console import Console

from src.bin.access import access


def update():
    _home_ = os.path.expanduser("~")
    console = Console()
    access(_home_)

    with console.status("[bold]> Updating repository ...[/bold]."):
        if not os.path.exists(f"{_home_}/repo"):
            console.log("[bold red][-] Local repository not found[/bold red]")
            console.log(
                "[bold bright_cyan][+] Cloning the repository.[/bold bright_cyan]"
            )
            os.system(
                f"git clone https://github.com/testno0/repo {_home_} &> /dev/null"
            )
        else:
            console.log("[bold bright_cyan][+] Pulling updates ...[/bold bright_cyan]")
            os.system(f"cd {_home_}/repo/ && git pull")

if __name__ == "__main__":
    update()
