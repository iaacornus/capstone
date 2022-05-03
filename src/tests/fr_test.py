from posixpath import expanduser
import face_recognition as fr
import sys
import cv2 as cv 
import numpy as np

from os.path import expanduser
from PIL import ImageDraw as imgd, Image as img

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

_PATH_ = f"{expanduser('~')}/devel/capstone/test_faces/"

biden_image = fr.load_image_file(f"{_PATH_}biden1.jpg")
bid_encode = fr.face_encodings(biden_image)[0]

biden_image2 = fr.load_image_file(f"{_PATH_}biden2.jpg")
bid2_fl = fr.face_locations(biden_image2)
bid2_encode = fr.face_encodings(biden_image2, bid2_fl)

obama_image = fr.load_image_file(f"{_PATH_}obama1.jpg")
obama_encode = fr.face_encodings(obama_image)[0]

obama_image2 = fr.load_image_file(f"{_PATH_}obama2.jpg")
obama2_encode = fr.face_encodings(obama_image2)[0]


# unknown_image = fr.load_image_file(f"{_PATH_}f2.jpg")
# u_encode = fr.face_encodings(unknown_image)[0]

# feed = cv.VideoCapture(0)

known_face_encodings = [
    obama_encode,
    bid_encode
]
known_face_names = [
    "Barack Obama",
    "Joe Biden"
]

pil_image = img.fromarray(biden_image2)
draw = imgd.Draw(pil_image)

for (top, right, bottom, left), face_encoding in zip(bid2_fl, bid2_encode):
    # See if the face is a match for the known face(s)
    matches = fr.compare_faces(known_face_encodings, face_encoding)

    name = "Unknown"

    face_distances = fr.face_distance(known_face_encodings, face_encoding)
    best_match_index = np.argmin(face_distances)
    if matches[best_match_index]:
        name = known_face_names[best_match_index]

    # Draw a box around the face using the Pillow module
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

    # Draw a label with a name below the face
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))


# Remove the drawing library from memory as per the Pillow docs
del draw

# Display the resulting image
pil_image.show()




"""results = fr.compare_faces([obama_encode], bid2_encode)

print("Is the unknown face a picture of Obama? {}".format(results))
# print("Is the unknown face a picture of Biden? {}".format(results[1]))
# print("Is the unknown face a new person that we've never seen before? {}".format(not True in results))"""