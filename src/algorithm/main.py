# python code for matching

from function import System
from os import system as sys
from os import chdir from sys import argv as INPT
from difflib import SequenceMatcher as SM

import os.path

# repo link is the link of this repository
# https://github.com/testno0/capstone
# although leave it blank as first, no one
# touchers the parameters

PWD = chdir(path.dirname(__file__))
sysINIT = System(PWD, <repo_link>)

"""
initiate the system, use try, except, else block
to catch errors and to organize the procedures based
on the cases the system gives.
"""

try:
    while True:
          if sysINIT.pullData() is True:
              break
          else:
              continue
              
except: # add other exceptions later
    """
    add more diagnostic messages later after setup
    of CLI application using argparse
    """
    raise SystemExit(0)
    
else:
    studentDATA, teacherDATA = sysINIT.getData()
    
    if (studentDATA is not True) or (teacherDATA is not True):
        pass
    else:
        sysINIT.getData()

finally:
    while True:
        cardID = INPUT[0]
        
        for ID in studentDATA:
            if SM(None, cardID, ID).ratio() == 1:
                pass
            else:
                pass
                """
                add more functinality later as described from
                methodology paper, refer to the pdf in manscript folder.
                """
        continue
