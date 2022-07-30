from os import walk
from os.path import exists
from typing import Any

from rich.console import Console
from face_recognition import (
    load_image_file,
    face_encodings
)

from src.utils.function import System, av_cams
from src.utils.face_recog import FaceRecog


def initiate(
        console: object,
        HOME: str,
    ) -> tuple[
            str, str, tuple[dict[str, list[str]], dict[str, list[str]]],
        ]:
    """Initiate the program."""

    with open(
            f"{HOME}/.easywiz/user_info", "r", encoding="utf-8"
        ) as info:
        source: list[str] = info.readlines()

    receiver_email: str = source[0].strip()
    school_name: str = source[3].strip()

    sys_initiate: object = System(
            HOME,
            "https://github.com/testno0/capstone",
            receiver_email
        )

    with console.status(
            "[bold magenta][+] Fetching data ...[/bold magenta]",
            spinner="simpleDots"
        ):
        if not exists(f"{HOME}/.easywiz/repo"):
            console.log(
                (
                    "[bold red][-] The repository is not setup."
                    "[/bold red] [bold magenta] [+] "
                    "Setting up the repository ...[/bold magenta]"
                )
            )
            data: tuple[
                    dict[str, list[str]], dict[str, list[str]]
                ] = sys_initiate.setup(school_name)[0]
        else:
            data: tuple[
                    dict[str, list[str]], dict[str, list[str]]
                ] =  sys_initiate.get_data()[0]

    return receiver_email, school_name, data


def main(HOME: str) -> None:
    console: object = Console()
    receiver_email, school_name, data = initiate(console, HOME)

    face_recog: object = FaceRecog(receiver_email, "Admin", school_name)

    PATH: str = f"{HOME}/.easywiz/repo/student_data/imgs/"
    IMGS_PATH: list[str] = []
    student_names: list[str] = []
    student_encodings: list[Any] = []

    with console.status(
            "[bold magenta][+] Fetching data ...[/bold magenta]",
            spinner="simpleDots"
        ):
        for name, std_data in data[1].items():
            console.log(
                (
                    f"[green]> [/green][cyan]{name}"
                    "[/cyan][green] appended ...[/green]"
                )
            )
            student_names.append(name)
            IMGS_PATH.append(f"{PATH}/{std_data[0]}")

    with console.status(
            "[bold magenta][>] Appending image encoding ...[/bold magenta]",
            spinner="simpleDots"
        ):
        for imgs in next(walk(IMGS_PATH)):
            try:
                img_file: Any = load_image_file(f"{IMGS_PATH}/{imgs}")
                img_encode: Any = face_encodings(img_file)
            except FileNotFoundError:
                continue
            else:
                if not not img_encode:
                    student_encodings.append(img_encode[0])

    # notify the user
    console.log("[bold green][+] System is ready.[/bold green]")

    av_cams_eval: bool = av_cams()

    while True:
        face_recog.face_recognition(
            av_cams_eval, face_encodings, student_names
        )
