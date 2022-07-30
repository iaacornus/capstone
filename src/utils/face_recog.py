from re import A
from typing import Any
from numpy import argmin, ndarray
from cv2 import (
    VideoCapture,
    resize,
    imshow,
    waitKey,
    destroyAllWindows
)
from face_recognition import (
    face_distance,
    compare_faces
)

from function import draw_rectangle


def face_recognition(
        av_cams: bool,
        known_fe: tuple[str] | list[str],
        known_fnames: tuple[str] | list[str]
    ) -> None:
    """Recognize the subject based on the face image."""

    process_this_frame: bool = True

    # initialize some variables include the encoded faces in the list
    face_locations: list[Any] = []
    face_encodings: list[Any] = []
    face_names: list[Any] = []

    if not av_cams:
        raise SystemExit("> There are no available cameras.")

    # video capture
    vid: object = VideoCapture(0)
    while True:
        # take frame and references from video capture
        _, frame = vid.read()

        # resizing to smaller frame, to avoid much larger use of gpu and
        # memory, also to decrease the processing time convert to
        # another color.
        small_frame = resize(frame, (0, 0), fx=0.25, fy=0.25)

        # convert to another color.
        rgb_small_frame = small_frame[:, :, ::-1]

        if process_this_frame:
            # get all the face endcoding and location in the current
            # frame returned by the live camera input.
            face_locations: ndarray = face_locations(rgb_small_frame)
            face_encodings: ndarray = face_encodings(
                    rgb_small_frame, face_locations
                )

            face_names: list[Any] = []
            for face_encoding in face_encodings:
                matches: Any = compare_faces(known_fe, face_encoding)
                name: str = "unknown"

                # Or instead, use the known face with the smallest
                # distance to the new face
                face_distances: Any = face_distance(known_fe, face_encoding)
                best_match_index: Any = argmin(face_distances)

                if matches[best_match_index]:
                    name: str = known_fnames[best_match_index]
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
        imshow("Video", frame)

        # hit 'q' on the keyboard to quit!
        if waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    destroyAllWindows()