import time
import os.path
import json

from sys import argv as Input
from os import system as Exec

class System:
    home = os.path.expanduser('~')

    def __init__(self, repository, _input_, dir) -> None:
        self.repository = repository
        self._input_ = _input_
    
    def fetchData(repository, home=home):
        if os.path.exists(f"{home}/repository") is False:
            Exec(f"git clone {repository} {home}/repository")
        else:
            Exec("git pull")
        
        try:
            with open(f"{home}/repository/student_data.json") as source:
                studentData = json.load(source)
                
            with open(f"{home}/repository/teacher_data.json") as Source:
                teacherData = json.load(Source)
                
        except FileNotFoundError or OSError or SystemError as e:
            raise SystemExit(f"\033[1;31m> {e} occured. Aborting.\033[0m")            
        except KeyboardInterrupt:
            raise SystemExit(f"\033[31;1m> Keyboard Interrupt. Aborting.\033[0m")
        else:
            return studentData, teacherData
        
    
