#!/home/edd1e/Desktop/stuff/studies/Programming/python_projects/profkit_project/prfkit_env/bin/python3.8


import subprocess
import re
from colorama import Style as Style2
import sys
import platform
import settings as s




############################




class mainApp:
    def __init__(self):
        pass
    
        def cmd_prompt(self):
            try:

                prompt = input(f'{s.prompt_arrow}')
                # if prompt == f'{s.add_student}':
                    



            except KeyboardInterrupt:
                print(f'{s.red}[ACTION ABORTED] You have exited profkit{s.re1}')


def MainApp():
    mainApp(sys.argv[1:])

