from os import walk
from os.path import exists
from typing import Any

from face_recognition import (
    load_image_file,
    face_encodings
)

from src.utils.function import System, av_cams
from src.utils.face_recog import FaceRecog
from src.misc.signs import Signs


def initiate(HOME: str) -> tuple[
        str, str, tuple[dict[str, list[str]], dict[str, list[str]]],
    ] | None:
    """Initiate the program."""

    print(f"{Signs.PROC} Fetching user credentials ...")
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

    print(f"{Signs.PROC} Fetching data from local repository ...")
    if not exists(f"{HOME}/.easywiz/repo"):
        raise FileNotFoundError
    else:
        try:
            data: tuple[
                    dict[str, list[str]], dict[str, list[str]]
                ] =  sys_initiate.get_data()[0]
        except FileNotFoundError:
            print(
                (
                    f"{Signs.FAIL} The repository not found.\n"
                    f"{Signs.PROC} Fetching the repository ..."
                )
            )
            data: tuple[
                    dict[str, list[str]], dict[str, list[str]]
                ] = sys_initiate.setup(school_name)[0]
        else:
            return receiver_email, school_name, data

    return None


def main(HOME: str) -> None:
    receiver_email, school_name, data = initiate(HOME)
    if receiver_email is None:
        raise SystemExit(
            f"{Signs.FAIL} Repository related error, aborting ..."
        )

    face_recog: object = FaceRecog(receiver_email, "Admin", school_name)

    PATH: str = f"{HOME}/.easywiz/repo/student_data/imgs/"
    IMGS_PATH: list[str] = []
    student_names: list[str] = []
    student_encodings: list[Any] = []

    print(
        f"{Signs.PROC} Processing fetched student data ..."
    )
    for name, std_data in data[1].items():
        print(f"{Signs.PASS} Student: {name} appended.")
        student_names.append(name)
        IMGS_PATH.append(f"{PATH}/{std_data[0]}")

    print(f"{Signs.PROC} Encoding faces ...")
    for imgs in next(walk(IMGS_PATH)):
        try:
            img_file: Any = load_image_file(f"{IMGS_PATH}/{imgs}")
            img_encode: Any = face_encodings(img_file)
        except FileNotFoundError:
            print(f"{Signs.FAIL} File is not found, skipping ...")
            continue
        else:
            if not not img_encode:
                print(f"{Signs.PASS} File successfully encoded.")
                student_encodings.append(img_encode[0])

    # notify the user
    print(f"{Signs.PASS} System is ready.")

    av_cams_eval: bool = av_cams()

    while True:
        face_recog.face_recognition(
            av_cams_eval, face_encodings, student_names
        )
