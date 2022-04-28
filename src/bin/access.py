import os.path
import sys
import os

from os import system as Exec

from code_email import Email

#* passed
# TODO : add system backup for email sending
# TODO : optimize the code

home = os.environ.get("HOME")

if os.path.exists("$HOME/.sys/create") is False:
    try:
        Exec(f"chmod +x {os.getcwd()}/setup.sh ; bash {os.getcwd()}/setup.sh")
    except KeyboardInterrupt:
        raise SystemExit("Operation Aborted.")

with open(f"{home}/.sys/user_info", 'r') as email:
    source = email.readlines()

receiver_email = source[0].rstrip().strip()
user = source[1].rstrip().strip()

email = Email(receiver_email, user)
app = sys.argv[1].strip()
trial = 0

while True:    
    if trial == 3:
        try:
            email.send_alert(receiver_email)
        except ConnectionError:
            pass
        finally:
            print("\033[91m> Too much error. Signing off.\033[0m")
            Exec("systemctl poweroff")
    elif trial >= 1:
        passphrase = email.send_phrase(receiver_email, user, dial=True)
    else:
        passphrase = email.send_phrase(receiver_email, user)
        
    trial += 1
    usr_inpt = str(input(f"\033[91m> Accessing {app}, sending the 24-key passphrase.\033[0m\n└─╼ Input the phrase sent to your email ({4-trial} left) : "))

    if usr_inpt == passphrase:
        break
    else:
        continue        

Exec(app)
Exec(f"killall {app} && killall gnome-terminal")
