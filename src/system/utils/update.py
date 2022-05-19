import sys
sys.path.append("..")

import os

from rich.console import Console

from bin.access import access


def update():
    HOME = os.path.expanduser("~")
    console = Console()

    if access(HOME):
        with console.status("[bold]> Updating repository ...[/bold]."):
            if not os.path.exists(f"{HOME}/repo"):
                console.log("[bold red][-] Local repository not found[/bold red]")
                console.log(
                    "[bold bright_cyan][+] Cloning the repository.[/bold bright_cyan]"
                )
                os.system(
                    f"git clone https://github.com/testno0/repo {HOME} &> /dev/null"
                )
            else:
                console.log("[bold bright_cyan][+] Pulling updates ...[/bold bright_cyan]")
                os.system(f"cd {HOME}/repo/ && git pull")
    else:
        os.system(f"rm -rf {HOME}/repo/")
        console.log("[bold red][-] Verification error.\n> Nuking the repository ...[/bold red]")
        os.system("systemctl poweroff")


if __name__ == "__main__":
    update()
