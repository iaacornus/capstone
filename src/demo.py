from os.path import expanduser

import face_recognition as fr
from rich.console import Console

from face_recog import face_recognition
from function import av_cams
from misc.colors import Color as C

def demo():
    console = Console()
    av_cams_ = av_cams()
    path_ = f"{expanduser('~')}/temporary/capstone/sample/"

    with console.status("[bold]> Loading face images ...[/bold]") as console:
        console.log("[bold]> Loading face images ...[/bold]")
        # load face references from path_.
        ref_face = fr.load_image_file(f"{path_}/test_1.png") # ezekiel lopez encoding
        ref_face_2 = fr.load_image_file(f"{path_}/test_2.png") # laisie angela donato encoding
        ref_face_3 = fr.load_image_file(f"{path_}/test_3.png") # nicole amber hennessey encoding
        ref_face_4 = fr.load_image_file(f"{path_}/test_4.png") # raven gose encoding
        ref_face_5 = fr.load_image_file(f"{path_}/test_5.png") # fiona leigh pagtama encoding

        console.log("[bold green]> Face loaded successfully.[/bold green]")

        #----------------------------------------------------------------
        # encode the faces.
        console.log(f"[bold]> Encoding faces ...[/bold]")
        rf_encoding = fr.face_encodings(ref_face)[0]
        rf_encoding2 = fr.face_encodings(ref_face_2)[0]
        rf_encoding3 = fr.face_encodings(ref_face_3)[0]
        rf_encoding4 = fr.face_encodings(ref_face_4)[0]
        rf_encoding5 = fr.face_encodings(ref_face_5)[0]

        console.log("[bold green]> Faces encoded successfully.[/bold green]")

    # load the function with the parameters it needs, unpack the tuple
    # for the decoding.
    with console.status("[bold]> Preparing function ...[/bold]") as console:
        face_recognition(
            av_cams_, console,
            face_encodings_= (
                ref_face,
                ref_face_2,
                ref_face_3,
                ref_face_4,
                ref_face_5
            ),
            face_names_= (
                "Ezekiel Lopez",
                "Laisie Angela Donato",
                "Nicole Amber Hennessey",
                "Raven Gose",
                "Fiona Leigh Pagtama",
            )
        )

demo()
