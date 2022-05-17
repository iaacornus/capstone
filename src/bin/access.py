import os

from rich.console import Console

from misc.colors import Colors as C
from bin.code_email import Email


def access(home_):
    console = Console()
    password, school_name = source[2].rstrip().strip(), source[3].rstrip().strip()
    email = Email(
        source[0].rstrip().strip(),
        source[1].rstrip().strip()
    )

    with open(f"{home_}/.att_sys/user_info") as info:
        source = info.readlines()

    try:
        trial, mark = 0, False

        while trial < 3:
            if not mark:
                print(f"{C.BOLD}", end="")
                verify = input(
                    f"> Kindly input your 32 character password ({3-trial} left): "
                )
                print(f"{C.END}", end="")

                if verify != password:
                    trial += 1
                    console.log(
                        f"[bold][red][-] Password doesn't match.[/red]{3-trial} left.[/bold]"
                    )
                    print(f"{C.BOLD}", end="")
                    send_new = input(
                        f"> Send a new temporary password to your email instead? [y/N]:"
                    )
                    print(f"{C.END}", end="")

                    if send_new in ['y', 'Y']:
                        mark = True
                    continue
                else:
                    return True
            else:
                new_pass = email.send("setup", school_name)
                print(f"{C.BOLD}", end="")
                verify_new = input(
                    f"> Kindly input your 32 character password (case sensitive {3-trial} left): "
                )
                print(f"{C.END}", end="")

                if verify_new != new_pass:
                    console.log(
                        f"[bold][red][-] Password doesn't match.[/red]{3-trial} left.[/bold]"
                    )
                    trial += 1
                    continue
                else:
                    return True
        else:
            email.send("alert", school_name)
            console.log(
                f"[bold red][-] Too much error, signing off.[/bold red]"
            )
            os.system("systemctl poweroff")

    except KeyboardInterrupt:
        os.system("systemctl poweroff")
