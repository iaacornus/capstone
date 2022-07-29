from argparse import ArgumentParser
from os import system
from os.path import expanduser
from rich.console import Console

from main import main
from demo import demo
from system.utils.update import update


def program_options():
    """
    This is an example use of the algorithm via cli program.
    """

    console = Console()

    description = (
            "This is a program designed to interact with"
            " face recognition algorithm Capstone Group 5."
        )
    parser = ArgumentParser(
            prog="EasyWiz",
            usage="EasyWiz [OPTIONS]",
            description=description
        )

    # all of the functions listed below prompts for the local or
    # temporary password email to the user using python's stdlib smtplib
    # and ssl, this requires internet connection, else the user need to
    # the password they received during the setup.

    # start/use the system
    parser.add_argument(
        "--use", "--use",
        help="Use the system.",
        action="store_true"
    )
    # update the database by calling the fetch database function from src.function
    parser.add_argument(
        "--update", "--update",
        help="Update the system",
        action="store_true"
    )
    # (re)setup the user
    parser.add_argument(
        "--setup", "--setup",
        help=(
                "Setup the user (prompts to input the "
                "passphrase sent via email, if used again)."
            ),
        action="store_true"
    )
    # destroy the system, can be used in case of intruder breach
    parser.add_argument(
        "--destroy", "--destroy",
        help="Destroy the user database.",
        action="store_true"
    )
    parser.add_argument(
        "--demo", "--demo",
        help="Face recognition demonstration.",
        action="store_true"
    )
    # show most of the background processes of the program
    parser.add_argument(
        "-v", "--verbose",
        help="Show the processes of program.",
        action="store_true"
    )

    args = parser.parse_args()

    try:
        if args.use:
            main(expanduser("~"), args.verbose) #? likely passing
        elif args.update:
            update() #* passed
        elif args.setup:
            system("./$HOME/.att_sys/system/setup.sh") #* passed
        elif args.destroy:
            system("echo 'rm -rf $HOME/.att_sys'") #* passed
        elif args.demo:
            demo()
    except ConnectionError: # add other exceptions later
        console.log("[bold red][-] Connection error.[/bold red]")
        raise SystemExit
    except KeyboardInterrupt:
        console.log("[bold red][-] Keyboard interrupt.[/bold red]")
        raise SystemExit
    except SystemError:
        console.log("[bold red][-] System error.[/bold red]")
        raise SystemExit


if __name__ == "__main__":
    program_options()
