from json import load
from typing_extensions import Self
from system import stdout
from os import system
from os.path import exists

from cv2 import (
    VideoCapture,
    FILLED,
    rectangle,
    FONT_HERSHEY_DUPLEX,
    putText
)
from rich.console import Console

from src.utils.access import access


def av_cams() -> bool:
    """Check the working cameras in the machine."""

    console: object = Console()
    index: int = 0
    cam_arr: list[int] = []

    with console.status(
            "[bold magenta][+] Checking for cameras ...[/bold magenta]",
            spinner="simpleDots"
        ):
        while True:
            cap = VideoCapture(index)

            if cap.read()[0]:
                cam_arr.append(index)
                cap.release()
                index += 1
                continue
            break

    if cam_arr:
        console.log("[bold green]> All available cameras found:[/bold green]")
        for num, cam in enumerate(cam_arr):
            console.log(f"[green]Camera: [/green][cyan]{num}, {cam}[/cyan]")

        input("Press any key to clear ...")
        stdout.write("\033[K") # remove the messages
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

    font = FONT_HERSHEY_DUPLEX
    putText(
        frame, name,
        (left + 6, bottom - 6),
        font, 1.0, (255, 255, 255), 1
    )


class System:
    """For initiation and setup of the program."""

    def __init__(self: Self, HOME: str, repo: str) -> None:
        self.HOME = HOME
        self.repo = repo
        self.PATH = f"{self.HOME}/.easywiz/repo"

    def pull_data(self: Self) -> bool:
        """Fetch the repository in the server."""

        try:
            if exists(f"{self.PATH}"):
                system(f"rm -rf {self.PATH}")

            system(f"mkdir -p {self.PATH}")
            system(f"git clone --branch database {self.repo}")
            system(f"mv {self.HOME}/capstone {self.PATH}")
        except (
                SystemError,
                KeyboardInterrupt,
                OSError,
                ConnectionError
            ):
            return False
        else:
            return True

    def get_data(self: Self) -> None:
        """Scrape the data from the pulled repository."""

        for _ in range(3):
            try:
                with open(
                        f"{self.PATH}/student_data/info.json",
                        "r",
                        encoding="utf-8"
                    ) as data_1:
                    student_data: dict[str, list[str]] = load(data_1)

                with open(
                        f"{self.PATH}/teacher_data/info.json",
                        "r",
                        encoding="utf-8"
                    ) as data_2:
                    teacher_data: dict[str, list[str]] = load(data_2)
            except FileNotFoundError:
                self.pull_data()
                continue
            else:
                return student_data, teacher_data

        raise SystemExit("> Too much error, please try again later.")

    def setup(self: Self) -> None:
        """Setup function."""

        if not access(self.HOME):
            raise SystemExit("> Too much error please try again later.")

        try:
            for _ in range(3):
                if not self.pull_data():
                    continue
                break
        except KeyboardInterrupt:
            raise SystemExit("> Too much error, please try again later.")
        else:
            return self.get_data()
