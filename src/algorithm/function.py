from os import system as sys
from os.path import exists

from bin.code_email import Email

import json

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
        try:
            with open(f"{self.HOME}/capstone/<filename>") as data:
                studentDATA = json.load(data)
                
            with open(f"{self.HOME}/capstone/<filename>") as Data:
                teacherDATA = json.load(Data)
                
            return studentDATA, teacherDATA
            
        except FileNotFoundError:
            while True:
                if self.pullData() is True:
                    return True, True
                else:
                    continue

    def setup(self):
        email = Email(self.admin_email)
        phrase = email.notify(setup=True)

        if self.phrase != phrase:
            raise SystemExit("Error")
        else:
            try:
                while True:
                    if self.pullData() is True:
                        break
                    else:
                        continue
            except:
                raise SystemExit("Error")
            else:
                return self.getData()

