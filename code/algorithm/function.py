from os import system as sys

import json

class System:
    def __init__(self, PWD, repo):
        self.PWD = PWD
        self.repo = repo
        
    def pullData(self, PWD, repo):
        try:
            if exits(f"{PWD}/<filename>") is True:
                sys("rm <filename>")
            sys(f"git clone {repo}")
        
            return True
        except SystemError, KeyboardInterrupt, OSError, ConnectionError:
            return False
            
    def getData():
        try:
            with open("<filename>") as data:
                studentDATA = json.load(data)
                
            with open("<filename>") as Data:
                teacherDATA = json.load(Data)
                
            return studentDATA, teacherDATA
            
        except FileNotFoundError:
            while True:
                if pullData() is True:
                    return True, True
                else:
                    continue
