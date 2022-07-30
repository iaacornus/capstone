from os import system

from src.utils.code_email import Email
from src.misc.signs import Signs


def access(HOME: str) -> None:
    """For repository access. Not fool proof."""

    print(f"{Signs.PROC} Fetching user credentials ...")
    with open(
            f"{HOME}/.easywiz/user_info", "r", encoding="utf-8"
        ) as info:
        source: list[str] = info.readlines()

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
                if input(
                    (
                        f"{Signs.INPT} Kindly input your 32"
                        f" character password ({3-n} left): "
                    )
                ) != password:
                    print(
                        f"{Signs.FAIL} Password didn't match. {3-n} left."
                    )
                    if input(
                        (
                            f"{Signs.INPT} Send a new temporary password"
                            " to your email instead? [y/N]: "
                        )
                    ).lower() == "y":
                        mark = True
                    continue
            else:
                if input(
                    (
                        f"{Signs.INPT} Kindly input your 32 character "
                        f"password (case sensitive {3-n} left): "
                    )
                ) != email.send("setup", school_name):
                    print(
                        f"{Signs.FAIL} Password didn't match. {3-n} left."
                    )
                    continue
            raise SystemExit

        email.send("alert", school_name)
        system(f"rm -rf {HOME}/repo/")
        raise KeyboardInterrupt
    except KeyboardInterrupt:
        print(f"{Signs.FAIL} Verification error.")
        system("systemctl poweroff")
