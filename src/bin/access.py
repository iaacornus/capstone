import sys
sys.path.append(".")

import os

from misc.colors import colors
from bin.code_email import Email


HOME = os.path.expanduser('~')
C = colors()


def access():
    with open(f"{HOME}/.att_sys/user_info") as info:
        source = info.readlines()
    
    receiver_email, user = source[0].rstrip().strip(), source[1].rstrip().strip() 
    password, school_name = source[2].rstrip().strip(), source[3].rstrip().strip()
    email = Email(receiver_email, user)

    try:
        trial, mark = 0, False
        
        while True:                  
            if trial == 3:
                try:
                    email.send("alert", school_name)
                except ConnectionError:
                    pass
                finally:
                    print(f"{C.BOLD+C.RED}> Too much error. Signing off.{C.END}")
                    #os.system("systemctl poweroff")

            if not mark:
                verify = input(f"{C.BOLD}> Kindly input your 32 character password (case sensitive {3-trial} left): {C.END}")

                if verify != password:
                    trial += 1
                    send_new = input(f"""\
                        {C.RED+C.BOLD}> Password doesn't match. {3-trial} left.{C.END}\n{C.BOLD}Send a new temporary password to your email instead? [y/N]: {C.END}""")
                
                    if send_new in ['y', 'Y']:
                        mark = True

                    continue
                else:
                    return True
                
            else:
                new_pass = email.send("setup", school_name)
                verify_new = input(f"""\
                    {C.BOLD}> Kindly input your 32 character password (case sensitive {3-trial} left): {C.END}""")
                
                if verify_new != new_pass:
                    print(f"{C.RED+C.BOLD}> Password doesn't match. {3-trial} left.{C.END}")
                    trial += 1
                    continue
                else:
                    return True
        
    except KeyboardInterrupt:
        print(f"{C.BOLD+C.RED}> Probable intruder. Signing off.{C.END}")   
        #os.system("systemctl poweroff")
