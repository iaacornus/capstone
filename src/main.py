import sys
import os

from rich.console import Console

from function import System, av_cams
from bin.code_email import Email
from face_recog import face_recognition


def main(_home_, verbose=False):
    """
    initiate the system, use try, except, else block to catch errors
    and to organize the procedures based on the cases the system gives.

    Returns
    -------
    None

    NOTES:
    console.log was used to display further information, this includes
    the time as well as line and source code file in the stdout.
    """

    with open(f"{_home_}/.att_sys/user_info", "r", encoding="utf-8") as info:
        source = info.readlines()

    path_ = f"{os.path.expanduser('~')}/.att_sys/capstone/student_data/imgs"
    receiver_email = source[0].rstrip().strip()
    school_name = source[3].rstrip().strip()
    student_data_proc = []

    console = Console()
    sys_initiate = System(
        _home_,
        "https://github.com/testno0/repo",
        receiver_email
    )

    with console.status(
            "[bold magenta][+] Fetching data ...[/bold magenta]", spinner="simpleDots"
        ):
        if not os.path.exists(f"{_home_}/repo"):
            console.log(
                "[bold red][-] The repository is not setup.[/bold red]"
                + "[bold magenta][+] Setting up the repository ...[/bold magenta]"
            )
            student_data, _ = sys_initiate.setup(school_name)
        else:
            student_data, _ = sys_initiate.get_data()

    with console.status(
            "[bold magenta][+] Fetching student names ...[/bold magenta]", spinner="simpleDots"
        ):
        if verbose: # for verbose
            student_names = []
            for name in student_data["name_init"]:
                console.log(
                    f"[green]> [/green][cyan]{name}[/cyan][green] appended ...[/green]"
                )
                student_names.append(name)
        else: # this is more optimized and faster, thus preferred
            student_names = list(student_data["name_init"])

    with console.status(
            "[bold magenta]> Processing student data ...[/bold]", spinner="simpleDots"
        ):
        for student in student_names:
            if verbose: # just print the student name and other information, and proceed
                        # with the iteration process.
                console.log(
                    f"[green]> Fetching data of [/green][cyan]{student}[/cyan] [green]...[/green]"
                )
            student_data_proc.append(student_data["student"])

    encoding_path = f"{_home_}/.att_sys/student_data/encoding.py"
    if not os.path.exists(encoding_path):
        with console.status(
                "[bold magenta]> Creating module for encoding ...[/bold magenta]", spinner="simpleDots"
            ):
            # initiate the file and add the needed import
            os.system(
                f"echo -e 'import face_recognition as fr \n\nclass Encoding:\n' > {encoding_path}"
            )
            for i in range(len(student_data_proc)-1):
                os.system(
                    f"echo '    face_ref_{i} = "
                    + f"fr.load_image_file({path_}/std{i}.png)' >> {encoding_path}"
                )

    # notify the user
    console.log("[bold green][+] System is ready.[/bold green]")
    sys.stdout.write("\033[K") # remove the messages

    email = Email(
        source[0].rstrip().strip(),
        source[1].rstrip().strip()
    )
    av_cams_eval = av_cams()

    while True:
        student = face_recognition(
            av_cams_eval,
            console,
            face_encodings_=tuple(student_data_proc), # use tuple to avoid mutations
            face_names_=tuple(student_names),
        )
        # some configurations for email function, can add more and can
        # be tweaked further for different use.
        if student:
            email.send(
                "student true",
                school_name,
                student_data["ID"]
            )
        else:
            console.log("Face is not {student} (recognized).")
            email.send(
                "student absent",
                school_name,
                student
            )
        continue
