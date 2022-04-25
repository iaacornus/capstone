from sys import argv as INPT
from difflib import SequenceMatcher as SM
from os import path

from function import System
from bin.code_email import Email

# repo link is the link of this repository https://github.com/testno0/capstone
# although leave it blank as first, no one touchers the parameters

HOME = path.expanduser('~')
sysINIT = System(HOME, "https://github.com/testno0/capstone")

""" initiate the system, use try, except, else block to catch errors and
to organize the procedures based on the cases the system gives. """

def main():
    try:
        studentDATA, teacherDATA = sysINIT.setup()
                
    except ConnectionError or KeyboardInterrupt or SystemError: # add other exceptions later
        """ add more diagnostic messages later after setup
        of CLI application using argparse """
        raise SystemExit(0)

    else:
        while True:
            cardID = INPT[0]
            
            for ID in studentDATA:
                if SM(None, cardID, ID).ratio() == 1:
                    pass
                else:
                    pass
                    """ add more functinality later as described from methodology
                    paper, refer to the pdf in manscript folder. """

            continue