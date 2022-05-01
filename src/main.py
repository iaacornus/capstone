import sys
sys.path.append(".")

from sys import argv as INPT, stdout
from difflib import SequenceMatcher as SM
from os import path
from time import sleep

from function import System
from bin.code_email import Email
from misc.colors import colors

# repo link is the link of this repository https://github.com/testno0/repo
# although leave it blank as first, no one touchers the parameters

HOME = path.expanduser('~')
sysINIT = System(HOME, "https://github.com/testno0/repo", phrase, admin_email)
C = colors()

""" initiate the system, use try, except, else block to catch errors and
to organize the procedures based on the cases the system gives. """

def main():
    try:
        print(f"{C.GREEN+C.BOLD}> Fetching data.{C.END}")
        if path.exists(f"{HOME}    def send(self, access, school_name, parent_name=None, teacher_name=None, student_name=None):/repo") is False:
            print(f"{C.GREEN+C.BOLD}> The repository is not setup. Setting up the repository.{C.END}")
            studentDATA, teacherDATA = sysINIT.setup()        
        else:
            studentDATA, teacherDATA = sysINIT.getData()

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
            cardID = INPT[0]
            
            for ID in studentDATA:
                if SM(None, cardID, ID).ratio() == 1:
                    print(f"{C.GREEN+C.BOLD}> Student recognized.{C.END}")
                    # def send(self, access, school_name, parent_name=None, teacher_name=None, student_name=None):
                    # leave at blank first
                    email.send("student true", school_name, parent_name=parent_name, teacher_name=teacher_name, student_name=student_name)
                else:
                    print(f"{C.RED+C.BOLD}> Error.{C.END}")
                    # leave at blank first
                    email.send("student false", school_name, parent_name=parent_name, teacher_name=teacher_name, student_name=student_name)

                    """ add more functinality later as described from methodology
                    paper, refer to the pdf in manscript folder. """

            continue