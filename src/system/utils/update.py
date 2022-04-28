import sys
sys.path.insert(0, "../..")

import os

from bin.access import main
from misc.colors import colors

HOME = os.path.expanduser('~')
C = colors()

ret = main()

if ret is True:
    if os.path.exists(f"{HOME}/repo") is True:        
        os.system("git clone https://github.com/testno0/repo $HOME/ &> /dev/null")
    else:
        print(f"{C.BOLD+C.GREEN} User system setup passed.{C.END}")
        os.system("cd {HOME}/repo/ && git pull")
else:
    # false phase, pass : #? passing
    os.system("rm -rf {HOME}/repo/")
    
    print(f"{C.BOLD+C.RED}> Verification error, repository was nuked by system for security.{C.END}")            
    #systemctl poweroff