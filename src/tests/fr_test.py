import face_recognition as fr
import sys
import numpy as np
import cv2 as cv

from os.path import expanduser

# this checks all the available web cams in computer and exits if there
# is none, and returns True or 1 if there is any

if __name__ == "__main__":
    __PATH__ = f"{expanduser('~')}/temporary/capstone/sample/"
    
    # load face
    ref_face = fr.load_image_file(f"{__PATH__}/test_1.png")    
    rf_encoding = fr.face_encodings(ref_face)[0]

    # video capture
    vid = cv.VideoCapture(0)

    # loop
    while True:   
        ret, frame = vid.read()
        small_frame = cv.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        cv.imshow('frame', frame)

        face_locations = fr.face_locations(rgb_small_frame)
        face_encodings = fr.face_encodings(rgb_small_frame, face_locations)

        for fe in face_encodings:
            matches = fr.compare_faces(rf_encoding, fe)

        for (top, right, bottom, left) in face_locations:
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)


        # Display the resulting image
        cv.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!
        if cv.waitKey(1) & 0xFF == ord('q'):
            break


vid.release()
cv.destroyAllWindows()