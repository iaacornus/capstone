from os import system
from os.path import expanduser, exists
from sys import stdout

from rich.console import Console

from function import System, av_cams
from bin.code_email import Email
from face_recog import face_recognition


def main(HOME: str, verbose: bool = False) -> None:
    with open(
            f"{HOME}/.att_sys/user_info", "r", encoding="utf-8"
        ) as info:
        source: list[str] = info.readlines()

    PATH: str = f"{expanduser('~')}/.att_sys/capstone/student_data/imgs"
    receiver_email: str = source[0].strip()
    school_name: str = source[3].strip()
    student_data_proc: list[str] = []

    console: object = Console()
    sys_initiate: object = System(
        HOME,
        "https://github.com/testno0/repo",
        receiver_email
    )

    with console.status(
            "[bold magenta][+] Fetching data ...[/bold magenta]",
            spinner="simpleDots"
        ):
        if not exists(f"{HOME}/repo"):
            console.log(
                (
                    "[bold red][-] The repository is not setup."
                    "[/bold red] [bold magenta] [+] "
                    "Setting up the repository ...[/bold magenta]"
                )
            )
            student_data: tuple[
                    dict[str, list[str]], dict[str, list[str]]
                ] = sys_initiate.setup(school_name)[0]
        else:
            student_data: tuple[
                    dict[str, list[str]], dict[str, list[str]]
                ] =  sys_initiate.get_data()

    with console.status(
            "[bold magenta][+] Fetching student names ...[/bold magenta]",
            spinner="simpleDots"
        ):
        if verbose: # for verbose
            student_names: list[str] = []
            for name in student_data["name_init"]:
                console.log(
                    (
                        f"[green]> [/green][cyan]{name}"
                        "[/cyan][green] appended ...[/green]"
                    )
                )
                student_names.append(name)
        else: # this is more optimized and faster, thus preferred
            student_names: list[str] = list(student_data["name_init"])

    with console.status(
            "[bold magenta]> Processing student data ...[/bold]",
            spinner="simpleDots"
        ):
        for student in student_names:
            if verbose: # just print the student name and other information, and proceed
                        # with the iteration process.
                console.log(
                    (
                        f"[green]> Fetching data of [/green]"
                        "[cyan]{student}[/cyan] [green]...[/green]"
                    )
                )
            student_data_proc.append(student_data["student"])

    encoding_path: str = f"{HOME}/.att_sys/student_data/encoding.py"
    if not exists(encoding_path):
        with console.status(
                "[bold magenta]> Creating encoding module ...[/bold magenta]",
                spinner="simpleDots"
            ):
            # initiate the file and add the needed import
            system(
                (
                    f"echo -e 'import face_recognition as fr"
                    " \n\nclass Encoding:\n' > {encoding_path}"
                )
            )
            for i in range(len(student_data_proc)-1):
                system(
                    (
                        f"echo '    face_ref_{i} = fr.load_image_file("
                        f"{PATH}/std{i}.png)' >> {encoding_path}"
                    )
                )

    # notify the user
    console.log("[bold green][+] System is ready.[/bold green]")
    stdout.write("\033[K") # remove the messages

    email: object = Email(
        source[0].strip(),
        source[1].strip()
    )
    av_cams_eval: bool = av_cams()

    while True:
        student = face_recognition(
                av_cams_eval,
                console,
                face_encodings_=tuple(student_data_proc), # use tuple to avoid mutations
                face_names_=tuple(student_names),
            )
        # some configurations for email function, can add more and can
        # be tweaked further for different use.
        # if student:
        #     email.send(
        #         "student true",
        #         school_name,
        #         student_data["ID"]
        #     )
        # else:
        #     console.log(f"Face is not {student}.")
        #     email.send(
        #         "student absent",
        #         school_name,
        #         student
        #     )
        # continue
