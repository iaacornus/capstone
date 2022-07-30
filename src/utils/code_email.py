from os import getlogin
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
from src.misc.signs import Signs


class Email:
    """Email reporting utility."""

    port: int = 465
    smtp_server: str = "smtp.gmail.com"
    sender_email: str = "clydebotrfid@gmail.com"
    password: str = "CCSHSRFIDG5"

    def __init__(
            self: Self, HOME: str, receiver_email: str, user: str
        ) -> None:
        self.receiver_email: str = receiver_email
        self.user: str = user

        with open(
                f"{HOME}/.easywiz/misc/msg/setup.msg", "r", encoding="utf-8"
            ) as setup_file, open(
                f"{HOME}/.easywiz/misc/msg/alert.msg", "r", encoding="utf-8"
            ) as alert_file, open(
                f"{HOME}/.easywiz/misc/msg/student.msg", "r", encoding="utf-8"
            ) as student_file, open(
                f"{HOME}/.easywiz/misc/msg/intruder.msg", "r", encoding="utf-8"
            ) as intruder_file:
            self.setup_msg: str = setup_file.read()
            self.alert_msg: str = alert_file.read()
            self.student_true_msg: str = student_file.read()
            self.intruder_msg: str = intruder_file.read()

    def send(
            self: Self,
            HOME: str,
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

        msg: object = EmailMessage()
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
        access = None

        match access:
            case "setup":
                msg["Subject"]: str = "Secure access phrase"
                msg.set_content(
                    (
                        self.setup_msg
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
            case "alert":
                msg["Subject"]: str = "Breach attempt alert."
                msg.set_content(
                    (
                        self.alert_msg
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
            case "student true":
                msg["Subject"]: str = f"{student_name} registered"
                msg.set_content(
                    (
                        self.student_true_msg
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
            case "intruder":
                msg["Subject"]: str = f"Intruder detection notice"
                msg.set_content(
                    (
                        self.intruder_msg
                            .replace(
                                "{RECEIVER_EMAIL}",
                                self.receiver_email
                            )
                            .replace(
                                "{SCHOOL_NAME}",
                                school_name
                            )
                            .replace(
                                "{USER}",
                                self.user
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
            case None:
                return False

        try:
            print(
                (
                    f"{Signs.PROC} Sending email ...\n{Signs.INFO}"
                    f" Receiver: {self.receiver_email}, context: {access}"
                )
            )
            context: SSLContext = create_default_context()
            with SMTP_SSL(
                    self.smtp_server,
                    self.port,
                    context=context
                ) as server:
                server.login(self.sender_email, self.password)
                server.send_message(msg)
        except ConnectionError:
            print(f"{Signs.FAIL} Connection error, email not sent.")
        else:
            print(f"{Signs.PASS} Email sent successfully.")
            return phrase

        return False
