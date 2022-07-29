from os import system
from rich.console import Console

from misc.colors import Colors as C
from bin.code_email import Email


def access(HOME):
    with open(
            f"{HOME}/.att_sys/user_info", "r", encoding="utf-8"
        ) as info:
        source = info.readlines()

    console = Console()
    password, school_name = (
            source[2].strip(), source[3].strip()
        )
    email = Email(
            source[0].strip(),
            source[1].strip()
        )
    mark = False

    try:
        for n in range(3):
            if not mark:
                verify = input(
                    (
                        f"{C.BOLD}> Kindly input your 32 character"
                        f" password ({3-n} left): {C.END}"
                    )
                )

                if verify != password:
                    console.log(
                        (
                            "[bold][red][-] Password doesn't match"
                            f".[/red]{3-n} left.[/bold]"
                        )
                    )
                    send_new = input(
                        (
                            f"{C.BOLD}> Send a new temporary password"
                            f" to your email instead? [y/N]: {C.END}"
                        )
                    )

                    if send_new in ['y', 'Y']:
                        mark = True
                    continue
            else:
                new_pass = email.send("setup", school_name)
                verify_new = input(
                    (
                        f"{C.BOLD}> Kindly input your 32 character "
                        f"password (case sensitive {3-n} left): {C.END}"
                    )
                )

                if verify_new != new_pass:
                    console.log(
                        (
                            "[bold][red][-] Password doesn't"
                            f" match.[/red]{3-n} left.[/bold]"
                        )
                    )
                    continue
            raise SystemExit

        email.send("alert", school_name)
        system(f"rm -rf {HOME}/repo/")
        console.log(
            (
                "[bold red][-] Verification error.\n"
                "> Nuking the repository ...[/bold red]"
            )
        )
        system("systemctl poweroff")

    except KeyboardInterrupt:
        system("systemctl poweroff")
