import face_recognition as fr
import numpy as np
import cv2 as cv

from function import draw_rectangle
from misc.colors import Colors as C


def face_recognition(av_cams, face_encodings_, face_names_):
    process_this_frame = True

    # initialize some variables include the encoded faces in the list
    known_fe, known_fnames = [], []
    face_locations, face_encodings, face_names = [], [], []

    if not av_cams:
        raise SystemExit(
            f"{C.BOLD+C.RED}> There are no available cameras.{C.END}"
        )
    # the names and the face encoding should the of the same size
    for fe_, fnames_ in zip(face_encodings_, face_names_):
        known_fe.append(fe_)
        known_fnames.append(fnames_)

    # video capture
    vid = cv.VideoCapture(0)
    while True:
        # take frame and references from video capture
        _, frame = vid.read()

        # resizing to smaller frame, to avoid much larger use of gpu and
        # memory, also to decrease the processing time convert to
        # another color.
        small_frame = cv.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # convert to another color.
        rgb_small_frame = small_frame[:, :, ::-1]

        if process_this_frame:
            # get all the face endcoding and location in the current
            # frame returned by the live camera input.
            face_locations = fr.face_locations(rgb_small_frame)
            face_encodings = fr.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                matches = fr.compare_faces(known_fe, face_encoding)
                name = "unknown"

                # Or instead, use the known face with the smallest
                # distance to the new face
                face_distances = fr.face_distance(known_fe, face_encoding)
                best_match_index = np.argmin(face_distances)

                if matches[best_match_index]:
                    name = known_fnames[best_match_index]
                face_names.append(name)

            for (top, right, bottom, left) in face_locations:
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                # output the box in the frame
                if name != "unknown":
                    draw_rectangle(
                        (0, 255, 0),
                        name, frame,
                        left, top,
                        right, bottom
                    )
                else:
                    draw_rectangle(
                        (0, 0, 255),
                        name, frame,
                        left, top,
                        right, bottom
                    )
        # display the resulting image
        cv.imshow("Video", frame)

        # hit 'q' on the keyboard to quit!
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    cv.destroyAllWindows()
