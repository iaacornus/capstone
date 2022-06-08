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
        phrase = "".join([random.choice(random.choice(str_set)) for x in range(32)])

        if access == "setup":
            msg["Subject"] = "Secure access phrase"
            msg.set_content(f"""\from misc.colors import Colors as C
                <!DOCTYPE html>
                <html>
                    </body>
                        <p align=justify>
                            Hello, TapTap is here to deliver the secure passphrase requested by: <b>{self.receiver_email} ({self.user}) from {school_name}.</b>,<br><br>
                            <em>DO NOT SHARE THIS CODE FOR USE IN SETUP/GIT PULL OF THE DATABASE</em>. This is the secure phrase for your access of the student and teacher data in repository setup: <br><br><center><b><code>{phrase}</code></b></center>
                        </p>

                        <p align=justify>
                            If you are not trying to access, ignore this email. The details of the computer are:<br><br>User: <i>{os.getlogin()}</i><br>HOSTNAME: <i>{socket.gethostname()}</i><br>IP address: <i>{socket.gethostbyname(socket.gethostname())}</i><br>Tracked from: <i>{geocoder.ip('me')}) at {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</i>.<blockquote>Cheers,<br>TapTap team</blockquote>
                        </p>
                    </body>
                </html>
                """,
                subtype="html"
            )

        elif access == "alert":
            msg["Subject"] = "Breach attempt alert."
            msg.set_content(f"""\
                <!DOCTYPE html>
                <html>
                    </body>
                        <p align=justify>
                            Hello, TapTap is here to alert <b>{self.receiver_email} ({self.user}) from {school_name} of possible breach alert.</b><br><br>
                            Your device has been receiving various passphrase mismatch. Due to the setup of device, it is shutting down as you receive this email. You can access it later on.
                        </p>

                        <p align=justify>
                            If you are not trying to access, ignore this email. The details of the computer are:<br><br>User: <i>{os.getlogin()}</i><br>HOSTNAME: <i>{socket.gethostname()}</i><br>IP address: <i>{socket.gethostbyname(socket.gethostname())}</i><br>Tracked from:<i> {geocoder.ip('me')}) at {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</i>.
                        </p>

                        <p align=justify>
                            This was done as security measure, the email in situation that met the criterion is inevitable.<br><blockquote>Cheers,<br>TapTap team</blockquote>
                        </p>
                    </body>
                </html>
                """,
                subtype="html"
            )

        elif access == "student true":
            msg["Subject"] = f"{student_name} registered"
            msg.set_content(f"""\
                <!DOCTYPE html>
                <html>
                    </body>
                        <p align=justify>
                            Hello, TapTap is here to notify that {student_name} of {school_name} has finally arrived his class at {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}, and is present in school today. Thank you!
                        </p>

                    </body>
                </html>
                """,
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
