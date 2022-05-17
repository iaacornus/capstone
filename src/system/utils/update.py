import sys
sys.path.append("..")

import os

from rich.console import Console

from bin.access import access
from misc.colors import colors as C


def update(setup):
    HOME = os.path.expanduser("~")
    console = Console()

    with console.status("[bold]> Updating repository ...[/bold]."):
        if access(HOME):
            if not os.path.exists(f"{HOME}/repo"):
                console.log(
                    "[bold red]>>> Local repository not found.[/bold red]\n"
                    + "[bold]>>> Cloning the repository ...[/bold]"
                )
                os.system(
                    f"git clone https://github.com/testno0/repo {HOME} &> /dev/null"
                )
            else:
                console.log("[bold]>>> Pulling updates ...[/bold]")
                os.system(f"cd {HOME}/repo/ && git pull")
        else:
            os.system(f"rm -rf {HOME}/repo/")
            print(
                f"{C.BOLD+C.RED}> Verification error",
                f"repository was nuked by system for security.{C.END}",
                end="\n"
            )
            #systemctl poweroff

if __name__ == "__main__":
    update()
