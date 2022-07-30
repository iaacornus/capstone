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

    with console.status(
            "[bold magenta][+] Loading user images ...[/bold magenta]",
            spinner="simpleDots"
        ):
        # load face references from PATH.
        # ezekiel lopez encoding
        ref_face: Any = load_image_file(f"{PATH}/test_1.png")
        # laisie angela donato encoding
        ref_face_2: Any = load_image_file(f"{PATH}/test_2.png")
        # nicole amber hennessey encoding
        ref_face_3: Any = load_image_file(f"{PATH}/test_3.png")
        # raven gose encoding
        ref_face_4: Any = load_image_file(f"{PATH}/test_4.png")
        # fiona leigh pagtama encoding
        ref_face_5: Any = load_image_file(f"{PATH}/test_5.png")

        console.log("[bold green]> Faces loaded successfully.[/bold green]")

    with console.status(
            "[bold magenta][+] Encoding user faces ...[/bold magenta]",
            spinner="simpleDots"
        ):
        #----------------------------------------------------------------
        # encode the faces.
        rf_encoding: Any = face_encodings(ref_face)[0]
        rf_encoding2: Any = face_encodings(ref_face_2)[0]
        rf_encoding3: Any = face_encodings(ref_face_3)[0]
        rf_encoding4: Any = face_encodings(ref_face_4)[0]
        rf_encoding5: Any = face_encodings(ref_face_5)[0]

        console.log("[bold green]> Faces encoded successfully.[/bold green]")

    # load the function with the parameters it needs, unpack the tuple
    # for the decoding.
    with console.status(
            "[bold magenta][+] Function running ...[/bold magenta]",
            spinner="simpleDots"
        ):
        face_recognition(
            av_cams_,
            face_encodings_= (
                    rf_encoding,
                    rf_encoding2,
                    rf_encoding3,
                    rf_encoding4,
                    rf_encoding5
                ),
            face_names_= (
                    "Ezekiel Lopez",
                    "Laisie Angela Donato",
                    "Nicole Amber Hennessey",
                    "Raven Gose",
                    "Fiona Leigh Pagtama",
                )
        )


if __name__ == "__main__":
    demo()
