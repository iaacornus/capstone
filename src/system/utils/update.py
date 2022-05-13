import sys
sys.path.append("..")

import os

from bin.access import access
from misc.colors import colors as C


def update():
    HOME = os.path.expanduser("~")
    
    if access(HOME):
        if not os.path.exists(f"{HOME}/repo"):        
            os.system(
                f"git clone https://github.com/testno0/repo {HOME} &> /dev/null"
            )
        else:
            print(f"{C.BOLD+C.GREEN} User system setup passed.{C.END}")
            os.system(f"cd {HOME}/repo/ && git pull")
    else:
        os.system(f"rm -rf {HOME}/repo/")        
        print(
            f"{C.BOLD+C.RED}> Verification error",
            f"repository was nuked by system for security.{C.END}"
        )            
        #systemctl poweroff

if __name__ == "__main__":
    update()