import face_recognition as fr
import cv2 as cv 
import numpy as np
import sys
from PIL import ImageDraw as id, Image as img

from misc.colors import colors

C = colors()

# this checks all the available web cams in computer and exits
# if there is none, and returns True or 1 if there is any
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

    if arr == []:
        pass
        # raise SystemExit(f"{C.RED+C.BOLD}> No camera available.{C.END}")
    else:
        input(f"\33[1;32m> All available cameras: {[num+' '+cam for num, cam in enumerate(arr)]}\33[0m\nPress any key to clear ...")
        sys.stdout.write("\033[K")
        return True

av_cams()



# feed = cv.VideoCapture(0)

