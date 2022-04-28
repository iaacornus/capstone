import random
import string
import smtplib
import ssl
import socket
import os
import geocoder

from datetime import datetime
from email.message import EmailMessage

class Email:
    port, smtp_server = 465, "smtp.gmail.com"
    sender_email, password = None, None # fill up later

    def __init__(self, receiver_email, user):
        self.receiver_email = receiver_email
        self.user = user

    def send(self, access, school_name, parent_name=None, teacher_name=None, student_name=None):
        msg, msg["From"], msg["To"] = EmailMessage(), self.sender_email, self.receiver_email
        phrase = ''.join([random.choice(random.choice([string.ascii_lowercase, string.ascii_uppercase, string.punctuation, string.digits])) for x in range(32)])
        
        if access == "setup": 
            msg["Subject"] = "Secure access phrase"
            msg.set_content(f"""\
            <!DOCTYPE html>
            <html>
                </body>
                    <p align=justify>
                        Hello, TapTap is here to deliver the secure passphrase requested by: <u><b>{self.receiver_email} ({self.user}) from {school_name}.</b></u>,<br><br>
                        <em>DO NOT SHARE THIS CODE FOR USE IN SETUP/GIT PULL OF THE DATABASE</em>. This is the secure phrase for your access of the student and teacher data in repository setup: <br><br><center><b><code>{phrase}</code></b></center>
                    </p>
                    
                    <p align=justify> 
                        If you are not trying to access from a computer with details of:<br><br>User: <i>{os.getlogin()}</i><br>HOSTNAME: <i>{socket.gethostname()}</i><br>IP address: <i>{socket.gethostbyname(socket.gethostname())}</i><br>Tracked from: {geocoder.ip('me')})<br> at {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}, ignore this email.<blockquote>Cheers,<br>TapTap team</blockquote>
                    </p>
                </body>
            </html>
            """, subtype="html")    
        
        elif access == "student true":
            msg["Subject"] = f"{student_name} registered"
            msg.set_content(f"""\
            <!DOCTYPE html>
            <html>
                </body>
                    <p align=justify>
                        Hello, TapTap is here to notify that {student_name} of {school_name} has finally arrived his class at {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}, and is present in school today. Thank you!
                    </p>
                    
                    <p align=justify> 
                        Other information of student in database:<br><br>Parent/Guardian: <i>{parent_name}</i><br>Teacher name:<i>{teacher_name}</i><blockquote>Cheers,<br>TapTap team</blockquote>
                    </p>
                </body>
            </html>
            """, subtype="html")            
        
        try:        
            """ Send the email to the user for the code."""            
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(self.smtp_server, self.port, context=context) as server:    
                server.login(self.sender_email, self.password)
                server.send_message(msg)
        
        except ConnectionError:
            return "Please try again later."
        
        else:
            return phrase if access is True else True
        