import sys
sys.path.append(".")

from sys import argv as INPT, stdout
from difflib import SequenceMatcher as SM
from os import path
from time import sleep

from function import System
from bin.code_email import Email
from misc.colors import colors as C

# repo link is the link of this repository https://github.com/testno0/repo
# although leave it blank as first, no one touchers the parameters

HOME = path.expanduser('~')

with open(f"{HOME}/.att_sys/user_info") as info:
    source = info.readlines()

receiver_email, user = source[0].rstrip().strip(), source[1].rstrip().strip() 
password, school_name = source[2].rstrip().strip(), source[3].rstrip().strip()
sysINIT = System(HOME, "https://github.com/testno0/repo", receiver_email)


def main(school_name=school_name, source=source):
    """initiate the system, use try, except, else block to catch errors
    and to organize the procedures based on the cases the system gives."""

    try:
        print(f"{C.GREEN+C.BOLD}> Fetching data.{C.END}")
        if not path.exists(f"{HOME}/repo"):
            print(f"""\
                {C.GREEN+C.BOLD}> The repository is not setup. Setting up the repository.{C.END}""")
            studentDATA, teacherDATA = sysINIT.setup(school_name)        
        else:
            studentDATA, teacherDATA = sysINIT.get_data()
    except ConnectionError: # add other exceptions later
        raise SystemExit(f"{C.RED+C.BOLD}> Connection Error.{C.END}")
    except KeyboardInterrupt:
        raise SystemExit(f"{C.RED+C.BOLD}> Keyboard Interrupt.{C.END}")
    except SystemError:
        raise SystemExit(f"{C.RED+C.BOLD}> System Error.{C.END}")
    else:
        # notify the user
        print(f"{C.GREEN+C.BOLD+C.BLINK}> System ready.{C.END}", end="\r")
        
        # init free time
        sleep(5)
        # remove the messages
        stdout.write("\033[K")
       
        email = Email()
        while True:
            pass
            cardID = INPT[0]            
                        
            for ID in studentDATA:
                if SM(None, cardID, ID).ratio() == 1:
                    print(f"{C.GREEN+C.BOLD}> Student recognized.{C.END}")
                    # def send(self, access, school_name, parent_name=None, teacher_name=None, student_name=None):
                    # leave at blank first
                    email.send("student true", source[3].rstrip().strip(), studentDATA[ID][0])
                else:
                    print(f"{C.RED+C.BOLD}> Error.{C.END}")
                    # leave at blank first
                    email.send("student true", source[3].rstrip().strip(), studentDATA)[ID][0]
            continue