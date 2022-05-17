import os

from misc.colors import Colors as C
from bin.code_email import Email


def access(home_):
    with open(f"{home_}/.att_sys/user_info") as info:
        source = info.readlines()

    password, school_name = source[2].rstrip().strip(), source[3].rstrip().strip()
    email = Email(
        source[0].rstrip().strip(),
        source[1].rstrip().strip()
    )

    try:
        trial, mark = 0, False

        while trial < 3:
            if not mark:
                print(f"{C.BOLD}")
                verify = input(
                    f"> Kindly input your 32 character password (case sensitive {3-trial} left): "
                )
                print(f"{C.END}")

                if verify != password:
                    trial += 1
                    print(
                        f"{C.RED+C.BOLD}> Password doesn't match. {3-trial} left.{C.END}{C.BOLD}"
                    )
                    send_new = input(
                        f"Send a new temporary password to your email instead? [y/N]:{C.END}"
                    )

                    if send_new in ['y', 'Y']:
                        mark = True
                    continue
                else:
                    return True

            else:
                new_pass = email.send("setup", school_name)
                print(f"{C.BOLD}")
                verify_new = input(
                    f"> Kindly input your 32 character password (case sensitive {3-trial} left): "
                )
                print(f"{C.END}")

                if verify_new != new_pass:
                    print(f"{C.RED+C.BOLD}> Password doesn't match. {3-trial} left.{C.END}")
                    trial += 1
                    continue
                else:
                    return True
        else:
            try:
                email.send("alert", school_name)
            except ConnectionError:
                pass # more error later
            finally:
                print(f"{C.BOLD+C.RED}> Too much error. Signing off.{C.END}")
                #os.system("systemctl poweroff")

    except KeyboardInterrupt:
        print(f"{C.BOLD+C.RED}> Probable intruder. Signing off.{C.END}")
        #os.system("systemctl poweroff")
