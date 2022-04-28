import sys
import os

from code_email import Email
from misc.colors import colors

#* passed
# TODO : add system backup for email sending
# TODO : optimize the code

def main():
    HOME = os.path.expanduser('~')
    C = colors()

    with open(f"{HOME}/.att_sys/user_info") as info:
        source = info.readlines()
        
    receiver_email, user, password = source[0].rstrip().strip(), source[1].rstrip().strip(), source[2].rstrip().strip()
    email = Email(receiver_email, user)

    
    trial, mark = 0, False

    while True:                  
        if trial == 3:
            try:
                email.alert(receiver_email)
            except ConnectionError:
                pass
            finally:
                print(f"{C.BOLD+C.RED}> Too much error. Signing off.{C.END}")
                os.system("systemctl poweroff")

        if mark is False:
            verify = input(f"> Kindly input your 32 character password (case sensitive {4-trial} left): ")

            if verify != password:
                trial += 1
                send_new = input(f"{C.BOLD}Send a new temporary password to your email instead? [y/N]: {C.END}")
            
                if send_new in ['y', 'Y']:
                    mark = True

                continue
            else:
                return True

        else:
            new_pass = email.notify(setup=True)
            verify_new = input(f"{C.BOLD+C.GREEN}> Kindly input your 32 character password (case sensitive {4-trial} left): ")
            
            if verify_new != new_pass:
                trial += 1
                continue
            else:
                return True
    
        return False