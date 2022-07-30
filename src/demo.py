from os import walk
from os.path import dirname
from typing import Any

from face_recognition import (
    load_image_file,
    face_encodings,
)
from rich.console import Console

from src.utils.face_recog import face_recognition
from src.utils.function import av_cams


def demo() -> None:
    """Function for demonstration of the algorithm."""

    console: object = Console()
    av_cams_: bool = av_cams()
    BASE_PATH: str = "/".join(dirname(__file__).split("/")[:-1])
    PATH: str = f"{BASE_PATH}/sample/"

    sample_encodings: list[Any] = []
    with console.status(
            "[bold magenta][+] Loading user images ...[/bold magenta]",
            spinner="simpleDots"
        ):
        # load face references from PATH.
        # ezekiel lopez encoding
        for imgs in next(walk(PATH)):
            try:
                img_file: Any = load_image_file(f"{PATH}/{imgs}")
            except FileNotFoundError:
                continue
            else:
                encodings: Any = face_encodings(img_file)
                if not not encodings:
                    sample_encodings.append(encodings)

        console.log("[bold green]> Faces encoded successfully.[/bold green]")

    # load the function with the parameters it needs, unpack the tuple
    # for the decoding.
    with console.status(
            "[bold magenta][+] Function running ...[/bold magenta]",
            spinner="simpleDots"
        ):
        face_recognition(
            av_cams_,
            sample_encodings,
            face_names_=(
                    "Ezekiel Lopez",
                    "Laisie Angela Donato",
                    "Nicole Amber Hennessey",
                    "Raven Gose",
                    "Fiona Leigh Pagtama",
                )
        )


if __name__ == "__main__":
    demo()
