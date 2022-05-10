import argparse
import sys
import os

from main import main
from function import System
from misc.colors import colors
from system.utils.update import update

C = colors()

def program_options():
    description = """\
        This is a program designed to interact with the TapTap, an RFID system designed by Capstone
        Group 5."""
    parser = argparse.ArgumentParser(prog="taptap",
                                        usage="taptap [OPTIONS]", description=description)

    # all of the functions listed below prompts for the local or temporary password email to the user
    # using python's stdlib smtplib and ssl, this requires internet connection, else the user need to
    # the password they received during the setup. 

    # start/use the system
    parser.add_argument("-use", "--use", help="Use the system.", action="store_true")
    # update the database by calling the fetch database function from src.function
    parser.add_argument("-U", "--update", help="Update the system", action="store_true")
    # (re)setup the user
    parser.add_argument(
            "-s",
            "--usersetup",
            help="Setup the user (prompts to input the passphrase sent via email, if used again).",
            action="store_true")
    # destroy the system, can be used in case of intruder breach
    parser.add_argument("-d", "--destroy", help="Destroy the user database.", action="store_true")    
        
    args = parser.parse_args()
    
    if args.use:
        main() #? likely passing
    elif args.update:
        update() #* passed
    elif args.usersetup:
        os.system("./$HOME/.att_sys/system/setup.sh") #* passed
    elif args.destroy:
        os.system("echo 'rm -rf $HOME/.att_sys'") #* passed

program_options()