import sys
sys.path.append(".")

import os

from code_email import Email
from misc.colors import colors

#? passed
# TODO : add system backup for email sending
# TODO : optimize the code


HOME = os.path.expanduser('~')
C = colors()

with open(f"{HOME}/.att_sys/user_info") as info:
    source = info.readlines()
    
receiver_email, user, password, school_name = source[0].rstrip().strip(), source[1].rstrip().strip(), source[2].rstrip().strip(), source[3].rstrip().strip()
email = Email(receiver_email, user)
trial, mark = 0, False

def access():
    try:
        while True:                  
            if trial == 3:
                try:
                    email.send("alert", school_name)
                except ConnectionError:
                    pass
                finally:
                    print(f"{C.BOLD+C.RED}> Too much error. Signing off.{C.END}")
                    os.system("systemctl poweroff")

            if mark is False:
                verify = input(f"{C.BOLD}> Kindly input your 32 character password (case sensitive {3-trial} left): {C.END}")

                if verify != password:
                    trial += 1
                    send_new = input(f"{C.BOLD}Send a new temporary password to your email instead? [y/N]: {C.END}")
                
                    if send_new in ['y', 'Y']:
                        mark = True

                    continue
                else:
                    return True
                
            else:
                new_pass = email.send("setup", school_name)
                verify_new = input(f"{C.BOLD}> Kindly input your 32 character password (case sensitive {3-trial} left): {C.END}")
                
                if verify_new != new_pass:
                    trial += 1
                    continue
                else:
                    return False
        
            return False
    except:
        print(f"{C.BOLD+C.RED}> Probable intruder. Signing off.{C.END}")   
        os.system("systemctl poweroff")
