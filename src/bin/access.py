import os

from misc.colors import colors as C
from bin.code_email import Email


def access():
    HOME = os.path.expanduser("~")
   
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
                    pass # more error later
                finally:
                    print(f"{C.BOLD+C.RED}> Too much error. Signing off.{C.END}")
                    #os.system("systemctl poweroff")

            if not mark:
                verify = input(f"""\
                    {C.BOLD}\r
                    > Kindly input your 32 character password (case sensitive {3-trial} left): 
                    {C.END}\r
                """)

                if verify != password:
                    trial += 1
                    print(f"{C.RED+C.BOLD}> Password doesn't match. {3-trial} left.{C.END}")
                    send_new = input(f"""\
                        {C.BOLD}Send a new temporary password to your email instead? [y/N]:{C.END}
                    """)
                
                    if send_new in ['y', 'Y']:
                        mark = True
                    continue
                else:
                    return True
                
            else:
                new_pass = email.send("setup", school_name)
                verify_new = input(f"""\
                    {C.BOLD}\r
                    > Kindly input your 32 character password (case sensitive {3-trial} left):
                    {C.END}\r
                """)
                
                if verify_new != new_pass:
                    print(f"{C.RED+C.BOLD}> Password doesn't match. {3-trial} left.{C.END}")
                    trial += 1
                    continue
                else:
                    return True
        
    except KeyboardInterrupt:
        print(f"{C.BOLD+C.RED}> Probable intruder. Signing off.{C.END}")   
        #os.system("systemctl poweroff")
