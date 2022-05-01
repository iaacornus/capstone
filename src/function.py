import sys
sys.path.append(".")

import json

from os import system as sys, path
from os.path import exists

from bin.code_email import Email

class System:
    def __init__(self, HOME, repo, phrase, admin_email):
        self.HOME = HOME
        self.repo = repo
        self.phrase = phrase
        self.admin_email = admin_email
        
    def pullData(self):
        try:
            if exists(f"{self.HOME}/capstone") is True:
                sys(f"rm -rf {self.HOME}/capstone")
            sys(f"git clone --branch database {self.repo}")
        
            return True
        except SystemError or KeyboardInterrupt or OSError or ConnectionError:
            return False
            
    def getData(self):
        count = 0

        while True:
            try:
                with open(f"{self.HOME}/repo/<filename>") as data:
                    studentDATA = json.load(data)
                    
                with open(f"{self.HOME}/repo/<filename>") as Data:
                    teacherDATA = json.load(Data)
                    
                return studentDATA, teacherDATA
                
            except FileNotFoundError:
                if self.pullData() is True:
                    continue
                else:
                    if count == 3:
                        raise SystemExit("Too much error, please try again later.")
                    count += 1
                    continue

    def setup(self):
        with open(f"{path.expanduser('~')}/.att_sys/user_info") as info:
            source = info.readlines()
    
        email = Email(self.admin_email, source[1].rstrip().strip())
        phrase = email.send("setup", source[3].rstrip().strip())

        if self.phrase != phrase:
            raise SystemExit("Error")
        else:
            try:
                while True:
                    if self.pullData() is not True:                    
                        continue
                    else:
                        break
            except:
                raise SystemExit("Error")
            else:
                studentDATA, teacherDATA = self.getData()
