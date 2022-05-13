import json
import cv2 as cv

from os import system as sys
from os.path import exists

from bin.access import access
from misc.colors import colors as C


def av_cams():
    index, arr = 0, []

    while True:
        cap = cv.VideoCapture(index)

        if not cap.read()[0]:
            break
        else:
            arr.append(index)
        cap.release()
        index += 1

    if not arr:
        pass
        # raise SystemExit(f"{C.RED+C.BOLD}> No camera available.{C.END}")
    else:
        print(
            f"{C.GREEN+C.BOLD}> All available cameras: {[f'{num} {cam}' for num, cam in enumerate(arr)]}{C.END}"
        )
        input("Press any key to clear ...")
        sys.stdout.write("\033[K")


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
    def __init__(self, HOME, repo, admin_email):
        self.HOME = HOME
        self.repo = repo
        self.admin_email = admin_email
        
    def pull_data(self):
        try:
            if exists(f"{self.HOME}/capstone"):
                sys(f"rm -rf {self.HOME}/capstone")
            sys(f"git clone --branch database {self.repo}")
        
            return True
        except SystemError or KeyboardInterrupt or OSError or ConnectionError:
            return False
            
    def get_data(self):
        count = 0

        while count < 3:
            try:
                with open(f"{self.HOME}/repo/<filename>") as data:
                    student_data = json.load(data)
                    
                with open(f"{self.HOME}/repo/<filename>") as Data:
                    teacher_data = json.load(Data)
                    
                return student_data, teacher_data
                
            except FileNotFoundError:
                self.pull_data()
                count += 1
                continue
        else:
            raise SystemExit(
                f"{C.BOLD+C.RED}> Too much error, please try again later.{C.END}"
            )

    def setup(self, school_name):
        ret = access()
        trial = 0

        if not ret:
            raise SystemExit(
                f"{C.BOLD+C.RED}> Too much error, please try again later.{C.END}"
            )
        else:
            try:
                while True:
                    if trial == 3:
                        break
                    
                    if self.pull_data() is not True:                    
                        trial += 1
                        continue
                    else:
                        break
            except KeyboardInterrupt:
                raise SystemExit(
                    f"{C.BOLD+C.RED}> Too much error, please try again later.{C.END}"
                )
            else:
                return self.get_data()