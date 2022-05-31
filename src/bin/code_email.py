import random
import smtplib
import ssl
import string
from datetime import datetime
import socket
from email.message import EmailMessage

class Email:
    def __init__(self, receiver_email, user):
        self.receiver_email = receiver_email
        self.user = user
    
    def send_phrase(self, receiver_email, user, dial=False):
        phrase = ''.join([random.choice(random.choice([string.ascii_letters, string.punctuation, string.digits])) for x in range(24)])
        
        port = 465
        smtp_server = "smtp.gmail.com"
        sender_email = None # fill up later
        password = None # fill up later
    
        msg = EmailMessage()
        msg["From"] = sender_email
        msg["To"] = receiver_email
    
        if dial is False:    
            msg["Subject"] = "Secure access phrase"
        
            msg.set_content(f"""\
            <!DOCTYPE html>
            <html>
                </body>
                    <p align=justify>
                        Hello <u><b>{receiver_email}</b></u>,<br><br>
                        DO NOT SHARE THIS CODE .This is the secure phrase for your access of the student and teacher data in repository setup : <br><br><center><b><code>{phrase}</code></b></center>
                    </p>
                    
                    <p align=justify> 
                    If you are not trying to access from a computer (user : <i>{user}</i>) with an IP address of <i>{socket.gethostbyname(socket.gethostname())}</i> and HOSTNAME : <i>{socket.gethostname()}</i> at {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}, ignore this email.<blockquote>Cheers,<br>Capstone Group 5</blockquote>
                    </p>
                </body>
            </html>
            """, subtype="html")
        elif dial is True:
            msg["Subject"] = "New secure access phrase"
        
            msg.set_content(f"""\
            <!DOCTYPE html>
            <html>
                </body>
                    <p align=justify>
                        Hello again <u><b>{receiver_email}</b></u>,<br><br>
                        Due to the access error, a new passphrase was sent. This is a new secure phrase for your access of the student and teacher data in the repository setup : <br><center><b><code>{phrase}</code></b></center>
                    </p>
                    
                    <p align=justify> 
                    If you are not trying to access from a computer (user : <i>{user}</i>) with an IP address of <i>{socket.gethostbyname(socket.gethostname())}</i> and HOSTNAME : <i>{socket.gethostname()}</i> at {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}, ignore this email.<blockquote>Cheers,<br>Capstone Group 5</blockquote>
                    </p>
                </body>
            </html>
            """, subtype="html")
            
        try:        
            """ Send the email to the user for the code."""            
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:    
                server.login(sender_email, password)
                server.send_message(msg)
        
        except ConnectionError:
            return "Please try again later."

        else:
            return phrase
    
