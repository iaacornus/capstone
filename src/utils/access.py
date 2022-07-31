from hashlib import sha256
from getpass import getpass
from os import system
from typing import NoReturn, TextIO

from src.utils.code_email import Email
from src.misc.signs import Signs


def access(HOME: str) -> None | NoReturn:
    """For repository access. Not fool proof."""

    print(f"{Signs.PROC} Fetching user credentials ...")
    with open(
            f"{HOME}/.easywiz/user_info", "r", encoding="utf-8"
        ) as info:
        info: TextIO
        source: list[str] = info.readlines()

    hash_ref: str = source[2].strip()
    school_name: str = source[3].strip()

    email: object = Email(
            HOME,
            source[0].strip(),
            source[1].strip()
        )

    try:
        for n in range(3):
            n: int
            password_inpt: str = getpass(
                    (
                        f"{Signs.INPT} Kindly input your 32"
                        f" character password ({3-n} left): "
                    )
                )
            passwd_hash: str = str(
                    sha256(password_inpt.encode("utf-8")).hexdigest()
                )

            if  passwd_hash == hash_ref:
                print(f"{Signs.PASS} Password matched, proceeding ...")
                break

            if input(
                (
                    f"{Signs.INPT} Send a new temporary password"
                    " to your email instead? [y/N]: "
                )
            ).lower() == "y":
                print(f"{Signs.PROC} Sending new temporary password ...")
                hash_ref: str = str(
                        sha256(
                            email.send("setup", school_name).encode("utf-8")
                        ).hexdigest()
                    )

            print(f"{Signs.FAIL} Password didn't match. {3-n} left.")

        system(f"rm -rf {HOME}/repo/")
        raise KeyboardInterrupt
    except KeyboardInterrupt:
        email.send("alert", school_name)
        print(f"{Signs.FAIL} Verification error.")
        system("systemctl poweroff")
