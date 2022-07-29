from os.path import expanduser

import face_recognition as fr
from rich.console import Console

from face_recog import face_recognition
from function import av_cams


def demo():
    console = Console()
    av_cams_ = av_cams()
    path_ = f"{expanduser('~')}/temporary/capstone/sample/"

    with console.status(
            "[bold magenta][+] Loading user images ...[/bold magenta]",
            spinner="simpleDots"
        ):
        # load face references from path_.
        # ezekiel lopez encoding
        ref_face = fr.load_image_file(f"{path_}/test_1.png")
        # laisie angela donato encoding
        ref_face_2 = fr.load_image_file(f"{path_}/test_2.png")
        # nicole amber hennessey encoding
        ref_face_3 = fr.load_image_file(f"{path_}/test_3.png")
        # raven gose encoding
        ref_face_4 = fr.load_image_file(f"{path_}/test_4.png")
        # fiona leigh pagtama encoding
        ref_face_5 = fr.load_image_file(f"{path_}/test_5.png")

        console.log("[bold green]> Faces loaded successfully.[/bold green]")

    with console.status(
            "[bold magenta][+] Encoding user faces ...[/bold magenta]",
            spinner="simpleDots"
        ):
        #----------------------------------------------------------------
        # encode the faces.
        rf_encoding = fr.face_encodings(ref_face)[0]
        rf_encoding2 = fr.face_encodings(ref_face_2)[0]
        rf_encoding3 = fr.face_encodings(ref_face_3)[0]
        rf_encoding4 = fr.face_encodings(ref_face_4)[0]
        rf_encoding5 = fr.face_encodings(ref_face_5)[0]

        console.log("[bold green]> Faces encoded successfully.[/bold green]")

    # load the function with the parameters it needs, unpack the tuple
    # for the decoding.
    with console.status(
            "[bold magenta][+] Function running ...[/bold magenta]",
            spinner="simpleDots"
        ):
        face_recognition(
            av_cams_,
            face_encodings_= (
                    rf_encoding,
                    rf_encoding2,
                    rf_encoding3,
                    rf_encoding4,
                    rf_encoding5
                ),
            face_names_= (
                    "Ezekiel Lopez",
                    "Laisie Angela Donato",
                    "Nicole Amber Hennessey",
                    "Raven Gose",
                    "Fiona Leigh Pagtama",
                )
        )


if __name__ == "__main__":
    demo()
