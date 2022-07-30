from os import getlogin
from os.path import expanduser
from random import choice
from string import (
    ascii_lowercase,
    ascii_uppercase,
    punctuation,
    digits
)
from socket import gethostbyname, gethostname
from datetime import datetime
from email.message import EmailMessage
from ssl import SSLContext, create_default_context
from smtplib import SMTP_SSL
from typing_extensions import Self

from geocoder import ip
from rich.console import Console


class Email:
    """Email reporting utility."""

    port: int = 465
    smtp_server: str = "smtp.gmail.com"
    sender_email: str = "clydebotrfid@gmail.com"
    password: str = "CCSHSRFIDG5"

    def __init__(self: Self, receiver_email: str, user: str) -> None:
        self.receiver_email: str = receiver_email
        self.user: str = user

    def send(
            self: Self,
            access: str,
            school_name: str,
            student_name: str = None
        ) -> bool | str:
        """Send email to the receiver.

        Arguments:
        access: str -- the type of email to send.
        school_name: str -- the name of the school.
        student_name: str -- name of the student.

        Returns false when an exception was raised, and return the
        phrase when the email was sent successfully.
        """

        console: object = Console()
        msg: object = EmailMessage()

        HOME: str = expanduser("~")

        msg["From"]: str = self.sender_email
        msg["To"]: str = self.receiver_email
        str_set: list[str] = [
                ascii_lowercase,
                ascii_uppercase,
                punctuation,
                digits
            ]

        phrase: str = "".join(
                [choice(choice(str_set)) for x in range(32)]
            )

        if access == "setup":
            with open(
                    f"{HOME}/.easywiz/misc/msg/setup.msg",
                    "r",
                    encoding="utf-8"
                ) as msg_file:
                msg: str = msg_file.read()

            msg["Subject"]: str = "Secure access phrase"
            msg.set_content(
                (
                    msg
                        .replace(
                            "{RECEIVER_EMAIL}",
                            self.receiver_email
                        )
                        .replace(
                            "{USER}",
                            self.user
                        )
                        .replace(
                            "{SCHOOL_NAME}",
                            school_name
                        )
                        .replace(
                            "{HOSTNAME}",
                            gethostname()
                        )
                        .replace(
                            "{USERNAME}",
                            getlogin()
                        )
                        .replace(
                            "{IP_ADDR}",
                            gethostbyname(gethostname())
                        )
                        .replace(
                            "{LOC}",
                            ip("me")
                        )
                        .replace(
                            "{DATETIME}",
                            datetime.now().strftime(
                                "%d/%m/%Y %H:%M:%S"
                            )
                        )

                ),
                subtype="html"
            )

        elif access == "alert":
            with open(
                    f"{HOME}/.easywiz/misc/msg/alert.msg",
                    "r",
                    encoding="utf-8"
                ) as msg_file:
                msg: str = msg_file.read()

            msg["Subject"]: str = "Breach attempt alert."
            msg.set_content(
                (
                    msg
                        .replace(
                            "{RECEIVER_EMAIL}",
                            self.receiver_email
                        )
                        .replace(
                            "{USER}",
                            self.user
                        )
                        .replace(
                            "{SCHOOL_NAME}",
                            school_name
                        )
                        .replace(
                            "{USERNAME}",
                            getlogin()
                        )
                        .replace(
                            "{HOSTNAME}",
                            gethostname()
                        )
                        .replace(
                            "{IP_ADDR}",
                            gethostbyname(gethostname())
                        )
                        .replace(
                            "{LOC}",
                            ip("me")
                        )
                        .replace(
                            "{DATETIME}",
                            datetime.now().strftime(
                                "%d/%m/%Y %H:%M:%S"
                            )
                        )
                ),
                subtype="html"
            )
            msg.set_content(
                f"""\

                """,
                subtype="html"
            )

        elif access == "student true":
            with open(
                    f"{HOME}/.easywiz/misc/msg/student_present.msg",
                    "r",
                    encoding="utf-8"
                ) as msg_file:
                msg: str = msg_file.read()

            msg["Subject"]: str = f"{student_name} registered"
            msg.set_content(
                (
                    msg
                        .replace(
                            "{STUDENT_NAME}",
                            student_name
                        )
                        .replace(
                            "{SCHOOL_NAME}",
                            school_name
                        )
                        .replace(
                            "{DATETIME}",
                            datetime.now().strftime(
                                "%d/%m/%Y %H:%M:%S"
                            )
                        )

                ),
                subtype="html"
            )
        try:
            with console.status(
                    "[bold magenta][+] Sending email ...[/bold magenta]",
                    spinner="simpleDots"
                ):
                context: SSLContext = create_default_context()

                with SMTP_SSL(
                        self.smtp_server,
                        self.port,
                        context=context
                    ) as server:
                    server.login(self.sender_email, self.password)
                    server.send_message(msg)
        except ConnectionError:
            console.log("[bold red][-] Connection error.[/bold red]")
        else:
            return phrase

        return False
