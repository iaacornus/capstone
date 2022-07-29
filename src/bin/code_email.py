import random
import string
import smtplib
import ssl
import socket
import os
from datetime import datetime
from email.message import EmailMessage

import geocoder
from rich.console import Console


class Email:
    port, smtp_server = 465, "smtp.gmail.com"
    sender_email, password = "clydebotrfid@gmail.com", "CCSHSRFIDG5" # fill up later

    def __init__(self, receiver_email, user):
        self.receiver_email = receiver_email
        self.user = user

    def send(self, access, school_name, student_name=None):
        console = Console()
        str_set = [
                string.ascii_lowercase,
                string.ascii_uppercase,
                string.punctuation,
                string.digits
            ]

        msg = EmailMessage()
        msg["From"] = self.sender_email
        msg["To"] = self.receiver_email
        phrase = "".join(
                [random.choice(random.choice(str_set)) for x in range(32)]
            )

        if access == "setup":
            with open("../msg/setup.msg", "r", encoding="utf-8") as msg_file:
                msg = msg_file.read()

            msg["Subject"] = "Secure access phrase"
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
                            socket.gethostname()
                        )
                        .replace(
                            "{USERNAME}",
                            os.getlogin()
                        )
                        .replace(
                            "{IP_ADDR}",
                            socket.gethostbyname(socket.gethostname())
                        )
                        .replace(
                            "{LOC}",
                            geocoder.ip("me")
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
            with open("../msg/setup.msg", "r", encoding="utf-8") as msg_file:
                msg = msg_file.read()

            msg["Subject"] = "Breach attempt alert."
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
                            os.getlogin()
                        )
                        .replace(
                            "{HOSTNAME}",
                            socket.gethostname()
                        )
                        .replace(
                            "{IP_ADDR}",
                            socket.gethostbyname(socket.gethostname())
                        )
                        .replace(
                            "{LOC}",
                            geocoder.ip("me")
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
            with open("../msg/setup.msg", "r", encoding="utf-8") as msg_file:
                msg = msg_file.read()

            msg["Subject"] = f"{student_name} registered"
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
                context = ssl.create_default_context()

                with smtplib.SMTP_SSL(
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
