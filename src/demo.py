from os import walk
from os.path import dirname
from typing import Any

from face_recognition import (
    load_image_file,
    face_encodings,
)

from src.utils.face_recog import face_recognition
from src.utils.function import av_cams
from src.misc.signs import Signs


def demo() -> None:
    """Function for demonstration of the algorithm."""

    BASE_PATH: str = "/".join(dirname(__file__).split("/")[:-1])
    PATH: str = f"{BASE_PATH}/sample/"
    av_cams_: bool = av_cams()

    print(f"{Signs.PROC} Encoding Images")

    sample_encodings: list[Any] = []
    for imgs in next(walk(PATH)):
        try:
            img_file: Any = load_image_file(f"{PATH}/{imgs}")
        except FileNotFoundError:
            continue
        else:
            encodings: Any = face_encodings(img_file)
            if not not encodings:
                sample_encodings.append(encodings)

    print(f"{Signs.PASS} Faces encoded successfully.")

    # load the function with the parameters it needs, unpack the tuple
    # for the decoding.
    print(f"{Signs.PROC} Running face recognition ...")
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
