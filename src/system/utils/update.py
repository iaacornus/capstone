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
            console.log("[bold magenta][+] Cloning the repository.[/bold magenta]")

            # clone the repository and redirect stdout to /dev/null, this is a secret
            os.system(
                f"git clone -b database https://github.com/testno0/capstone {_home_} &> /dev/null"
            )
        else:
            console.log("[bold magenta][+] Pulling updates ...[/bold magenta]")
            os.system(f"cd {_home_}/.att_sys/repo/ && git pull")

if __name__ == "__main__":
    update()
