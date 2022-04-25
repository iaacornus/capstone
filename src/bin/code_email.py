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
    def __init__(self, receiver_email):
        self.receiver_email = receiver_email
    
    def notify(self, dial=False, setup=False):        
        port, smtp_server = 465, "smtp.gmail.com"
        sender_email, password = None, None # fill up later
        msg, msg["From"], msg["To"] = EmailMessage(), sender_email, self.receiver_email
        phrase = ''.join([random.choice(random.choice([string.ascii_lowercase, string.ascii_uppercase, string.punctuation, string.digits])) for x in range(32)])

        if setup is True:
            msg["Subject"] = "Secure access phrase"

            msg.set_content(f"""\
            <!DOCTYPE html>
            <html>
                </body>
                    <p align=justify>
                        Hello <u><b>{self.receiver_email}</b></u>,<br><br>
                        <em>DO NOT SHARE THIS CODE FOR USE IN SETUP/GIT PULL OF THE DATABASE</em>. This is the secure phrase for your access of the student and teacher data in repository setup: <br><br><center><b><code>{phrase}</code></b></center>
                    </p>
                    
                    <p align=justify> 
                    If you are not trying to access from a computer with details of:<br><br>(User: <i>{os.getlogin()}</i>)<br>HOSTNAME: <i>{socket.gethostname()}</i><br>IP address: <i>{socket.gethostbyname(socket.gethostname())}</i><br>Tracked from: {geocoder.ip('me')})<br> at {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}, ignore this email.<blockquote>Cheers,<br>Capstone Group 5</blockquote>
                    </p>
                </body>
            </html>
            """, subtype="html")    

        else:
            if dial is False:    
                msg["Subject"] = "Secure access phrase"
            
                msg.set_content(f"""\
                <!DOCTYPE html>
                <html>
                    </body>
                        <p align=justify>
                            Hello <u><b>{self.receiver_email}</b></u>,<br><br>
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
                            Hello again <u><b>{self.receiver_email}</b></u>,<br><br>
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
    
    def alert(self, dial=False, setup=False):        
        port, smtp_server = 465, "smtp.gmail.com"
        sender_email, password = None, None # fill up later
        msg, msg["From"], msg["To"] = EmailMessage(), sender_email, self.receiver_email
        phrase = ''.join([random.choice(random.choice([string.ascii_lowercase, string.ascii_uppercase, string.punctuation, string.digits])) for x in range(32)])

        if setup is True:
            msg["Subject"] = "Secure access phrase"

            msg.set_content(f"""\
            <!DOCTYPE html>
            <html>
                </body>
                    <p align=justify>
                        Hello <u><b>{self.receiver_email}</b></u>,<br><br>
                        <em>DO NOT SHARE THIS CODE FOR USE IN SETUP/GIT PULL OF THE DATABASE</em>. This is the secure phrase for your access of the student and teacher data in repository setup: <br><br><center><b><code>{phrase}</code></b></center>
                    </p>
                    
                    <p align=justify> 
                    If you are not trying to access from a computer with details of:<br><br>(User: <i>{os.getlogin()}</i>)<br>HOSTNAME: <i>{socket.gethostname()}</i><br>IP address: <i>{socket.gethostbyname(socket.gethostname())}</i><br>Tracked from: {geocoder.ip('me')})<br> at {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}, ignore this email.<blockquote>Cheers,<br>Capstone Group 5</blockquote>
                    </p>
                </body>
            </html>
            """, subtype="html")    

        else:
            if dial is False:    
                msg["Subject"] = "Secure access phrase"
            
                msg.set_content(f"""\
                <!DOCTYPE html>
                <html>
                    </body>
                        <p align=justify>
                            Hello <u><b>{self.receiver_email}</b></u>,<br><br>
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
                            Hello again <u><b>{self.receiver_email}</b></u>,<br><br>
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
    
