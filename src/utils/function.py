from json import load
from shutil import move
from typing_extensions import Self
from os import system, mkdir, remove
from os.path import exists
from typing import Any, NoReturn, TextIO

from cv2 import (
    VideoCapture,
    FILLED,
    rectangle,
    FONT_HERSHEY_DUPLEX,
    putText
)

from src.utils.access import access
from src.misc.signs import Signs


def av_cams() -> bool:
    """Check the working cameras in the machine."""

    index: int = 0
    cam_arr: list[int] = []

    print(f"{Signs.PROC} Searching for available cameras ...")
    while True:
        cap: Any = VideoCapture(index)

        if cap.read()[0]:
            print(f"{Signs.PASS} Camera: {index} found.")
            cam_arr.append(index)
            cap.release()
            index += 1
            continue
        break

    if cam_arr:
        print(f"{Signs.INFO} All available cameras found:")
        for num, cam in enumerate(cam_arr):
            print(f"\tCamera: {num}, {cam}")

        return True

    return False


def draw_rectangle(
        color: str,
        name: str,
        frame: tuple[int, int, int],
        left: int,
        top: int,
        right: int,
        bottom: int
    ) -> None:
    """Draw a rectangle in the detected face of the subject.

    Arguments:
    color: str -- the color of the rectangle border.
    name: str -- identified name of the subject.
    frame: tuple[int, int, int] -- size of the frame.
    left: int, top: int, right: int, bottom: int -- end coordinates of
        the face of the subject.
    """

    rectangle(
        frame,
        (left, top),
        (right, bottom),
        color, 2
    )

    rectangle(
        frame,
        (left, bottom - 35),
        (right, bottom),
        color, FILLED
    )

    font: int = FONT_HERSHEY_DUPLEX
    putText(
        frame, name,
        (left + 6, bottom - 6),
        font, 1.0, (255, 255, 255), 1
    )


class System:
    """For initiation and setup of the program."""

    def __init__(self: Self, HOME: str, repo: str) -> None:
        self.HOME: str = HOME
        self.repo: str = repo
        self.PATH: str = f"{self.HOME}/.easywiz/repo"

    def pull_data(self: Self) -> bool:
        """Fetch the repository in the server."""

        try:
            print(
                f"{Signs.PROC} Pulling data from remote repository ..."
            )
            if exists(f"{self.PATH}"):
                remove(self.PATH)

            mkdir(self.PATH)
            system(f"git clone --branch database {self.repo}")
            move(f"{self.HOME}/capstone", self.PATH)
        except (
                SystemError,
                KeyboardInterrupt,
                OSError,
                ConnectionError
            ) as Err:
            print(f"{Signs.FAIL} {Err}, retrying ...")
            return False
        else:
            print(f"{Signs.PASS} Repository fetched.")
            return True

    def get_data(self: Self) -> None | NoReturn:
        """Scrape the data from the pulled repository."""

        for _ in range(3):
            try:
                print(
                    f"{Signs.PROC} Scraping data from local repository ..."
                )
                with open(
                        f"{self.PATH}/student_data/info.json",
                        "r",
                        encoding="utf-8"
                    ) as data_1:
                    data_1: TextIO
                    student_data: dict[str, list[str]] = load(data_1)

                with open(
                        f"{self.PATH}/teacher_data/info.json",
                        "r",
                        encoding="utf-8"
                    ) as data_2:
                    data_2: TextIO
                    teacher_data: dict[str, list[str]] = load(data_2)
            except FileNotFoundError:
                print(
                    f"{Signs.FAIL} File not found, fetching repository ..."
                )
                self.pull_data()
                continue
            else:
                print(
                    f"{Signs.PASS} Student and teacher data fetched."
                )
                return student_data, teacher_data

        raise SystemExit(
            f"{Signs.FAIL} Too much error, aborting ..."
        )

    def setup(self: Self) -> None | NoReturn:
        """Setup function."""

        if not access(self.HOME):
            raise SystemExit(
                f"{Signs.FAIL} Too much error, aborting ..."
            )

        try:
            for _ in range(3):
                if not self.pull_data():
                    continue
                break
        except KeyboardInterrupt:
            raise SystemExit(
                f"{Signs.FAIL} Too much error, aborting ..."
            )
        else:
            print(f"{Signs.PASS} Repository data fetched successfully.")
            return self.get_data()
