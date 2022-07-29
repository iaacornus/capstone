from json import load
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

from bin.access import access
from misc.colors import Colors as C


def av_cams():
    console = Console()
    index, cam_arr = 0, []

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


def draw_rectangle(color, name, frame, left, top, right, bottom):
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
    def __init__(self, HOME, repo):
        self.HOME = HOME
        self.repo = repo
        self.PATH = f"{self.HOME}/repo"

    def pull_data(self):
        try:
            if exists(f"{self.PATH}"):
                system(f"rm -rf {self.PATH}")

            system(f"git clone --branch database {self.repo}")
            system(f"mv {self.HOME}/capstone {self.PATH}")
            return True

        except (
                SystemError,
                KeyboardInterrupt,
                OSError,
                ConnectionError
            ):
            return False

    def get_data(self):
        for _ in range(3):
            try:
                with open(
                        f"{self.PATH}/student_data/info.json",
                        "r",
                        encoding="utf-8"
                    ) as data_1:
                    student_data = load(data_1)

                with open(
                        f"{self.PATH}/teacher_data/info.json",
                        "r",
                        encoding="utf-8"
                    ) as data_2:
                    teacher_data = load(data_2)

                return student_data, teacher_data
            except FileNotFoundError:
                self.pull_data()
                count += 1
                continue

        raise SystemExit(
            f"{C.BOLD+C.RED}> Too much error, please try again later.{C.END}"
        )

    def setup(self):
        if not access(self.HOME):
            raise SystemExit(
                (
                    f"{C.BOLD+C.RED}> Too much error"
                    ", please try again later.{C.END}"
                )
            )

        try:
            for _ in range(3):
                if not self.pull_data():
                    continue
                break
        except KeyboardInterrupt:
            raise SystemExit(
                (
                    f"{C.BOLD+C.RED}> Too much error"
                    ", please try again later.{C.END}"
                )
            )
        else:
            return self.get_data()
