import sys
sys.path.append(".")

import json

from os import system as sys, path
from os.path import exists

from bin.code_email import Email
from bin.access import access
from misc.colors import colors

class System:
    C = colors()
    
    def __init__(self, HOME, repo, admin_email):
        self.HOME = HOME
        self.repo = repo
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
            if count == 3:
                raise SystemExit(f"{self.C.BOLD+self.C.RED}> Too much error, please try again later.{self.C.END}")

            try:
                with open(f"{self.HOME}/repo/<filename>") as data:
                    studentDATA = json.load(data)
                    
                with open(f"{self.HOME}/repo/<filename>") as Data:
                    teacherDATA = json.load(Data)
                    
                return studentDATA, teacherDATA
                
            except FileNotFoundError:
                self.pullData()
                count += 1
                continue

    def setup(self, school_name):
        ret = access()
        trial = 0

        if ret is False:
            raise SystemExit(f"{self.C.BOLD+self.C.RED}> Too much error, please try again later.{self.C.END}")
        else:
            try:
                while True:
                    if trial == 3:
                        break
                    
                    if self.pullData() is not True:                    
                        trial += 1
                        continue
                    else:
                        break
            except KeyboardInterrupt:
                raise SystemExit(f"{self.C.BOLD+self.C.RED}> Too much error, please try again later.{self.C.END}")
            else:
                studentDATA, teacherDATA = self.getData()
