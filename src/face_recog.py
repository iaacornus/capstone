from os.path import expanduser

import face_recognition as fr
import numpy as np
import cv2 as cv

from function import draw_rectangle


def face_recognition(av_cams):
    path_ = f"{expanduser('~')}/temporary/capstone/sample/"
    if not av_cams:
        pass
    
    # load face references from path_.
    # ezekiel lopez encoding
    ref_face = fr.load_image_file(f"{path_}/test_1.png")    
    rf_encoding = fr.face_encodings(ref_face)[0]

    # laisie angela donato encoding
    ref_face_2 = fr.load_image_file(f"{path_}/test_2.png")
    rf_encoding2 = fr.face_encodings(ref_face_2)[0]

    known_fe = [
        rf_encoding,
        rf_encoding2,    
    ]
    known_fnames = [
        "Ezekiel Lopez",
        "Laisie Angela Donato",
    ]
        
    # Initialize some variables
    face_locations, face_encodings, face_names = [], [], []     
    process_this_frame = True
    
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
                    return True
                else:
                    draw_rectangle(
                        (0, 0, 255),
                        name, frame,
                        left, top,
                        right, bottom
                    )
                    return False
        # display the resulting image
        cv.imshow("Video", frame)

        # hit 'q' on the keyboard to quit!
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    cv.destroyAllWindows()