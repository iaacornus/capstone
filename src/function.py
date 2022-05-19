import json
from sys import stdout
from os import system as sys
from os.path import exists

import cv2 as cv
from rich.console import Console

from bin.access import access
from misc.colors import Colors as C


def av_cams():
    console = Console()
    index, cam_arr = 0, []

    with console.status(
            "[bold bright_cyan][+] Checking for available cameras ...[/bold bright_cyan]",
            spinner="simpleDots"
        ):
        while True:
            cap = cv.VideoCapture(index)

            if cap.read()[0]:
                cam_arr.append(index)
                cap.release()
                index += 1
                continue
            break

    if not cam_arr:
        return False
    else:
        console.log(
            f"[bold green]> All available cameras found:[/bold green]"
        )
        for num, cam in enumerate(cam_arr):
            console.log(
                f"[green]Camera: [/green][cyan]{num}, {cam}[/cyan]"
            )
        input("Press any key to clear ...")
        stdout.write("\033[K") # remove the messages
        return True


def draw_rectangle(color, name, frame, left, top, right, bottom):
    cv.rectangle(
        frame,
        (left, top),
        (right, bottom),
        color, 2
    )

    cv.rectangle(
        frame,
        (left, bottom - 35),
        (right, bottom),
        color, cv.FILLED
    )

    font = cv.FONT_HERSHEY_DUPLEX
    cv.putText(
        frame, name,
        (left + 6, bottom - 6),
        font, 1.0, (255, 255, 255), 1
    )


class System:
    def __init__(self, HOME, repo):
        self.HOME = HOME
        self.repo = repo

    def pull_data(self):
        try:
            if exists(f"{self.HOME}/repo"):
                sys(f"rm -rf {self.HOME}/repo")

            sys(f"git clone --branch database {self.repo}")
            sys(f"mv {self.HOME}/capstone {self.HOME}/repo")
            return True

        except SystemError or KeyboardInterrupt or OSError or ConnectionError:
            return False

    def get_data(self):
        count = 0

        while count < 3:
            try:
                with open(f"{self.HOME}/repo/student_data/info.json") as data:
                    student_data = json.load(data)

                with open(f"{self.HOME}/repo/teacher_data/info.json") as Data:
                    teacher_data = json.load(Data)

                return student_data, teacher_data

            except FileNotFoundError:
                self.pull_data()
                count += 1
                continue

        raise SystemExit(
            f"{C.BOLD+C.RED}> Too much error, please try again later.{C.END}"
        )

    def setup(self):
        trial = 0

        if not access(self.HOME):
            raise SystemExit(
                f"{C.BOLD+C.RED}> Too much error, please try again later.{C.END}"
            )

        try:
            while trial < 3:
                if not self.pull_data():
                    trial += 1
                    continue
                break
        except KeyboardInterrupt:
            raise SystemExit(
                f"{C.BOLD+C.RED}> Too much error, please try again later.{C.END}"
            )
        else:
            return self.get_data()
