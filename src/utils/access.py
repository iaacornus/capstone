from os import system
from rich.console import Console

from src.utils.code_email import Email


def access(HOME) -> None:
    """For repository access. Not fool proof."""

    with open(
            f"{HOME}/.att_sys/user_info", "r", encoding="utf-8"
        ) as info:
        source: list[str] = info.readlines()

    console: object = Console()
    password: str = source[2].strip()
    school_name: str = source[3].strip()

    email: object = Email(
            source[0].strip(),
            source[1].strip()
        )
    mark: bool = False

    try:
        for n in range(3):
            if not mark:
                verify: str = input(
                    "> Kindly input your 32 character password ({3-n} left): "
                )

                if verify != password:
                    console.log(
                        (
                            "[bold][red][-] Password doesn't"
                            " match .[/red]{3-n} left.[/bold]"
                        )
                    )
                    send_new: str = input(
                        (
                            "> Send a new temporary password"
                            " to your email instead? [y/N]: "
                        )
                    )

                    if send_new in ['y', 'Y']:
                        mark = True
                    continue
            else:
                new_pass: str | bool = email.send("setup", school_name)
                verify_new: str = input(
                    (
                        "> Kindly input your 32 character "
                        f"password (case sensitive {3-n} left): "
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
