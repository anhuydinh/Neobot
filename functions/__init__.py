#Installing Tool's settings
# from .func1 import function1
from main import *
import time
import sys
import string
import os
from tqdm import *


print("test message") #Check if __init__ works
def clear_scr():
    os.system("clear")

def loading(time_load,message): #For Decorative reason
    for i in tqdm(range(time_load), desc = str(message)):
        time.sleep(0.5)

def check_logs():
    if os.path.isdir('logs') == True:
        print("required files present")
        sys.stdout.write("Required files present")
    else: #
        print("No logs file found\n")
        os.mkdir("logs")
        if os.path.isdir('logs') == True: #
            print("logs folder initiated")
            
        elif os.path.isdir('logs')== False: #
            print('Logs folder error')
            os.mkdir('logs')
            print("logs created")

class function1():

    def readCookies():
        directry = str(cookiesfile+".txt")
        lines = []
        with open(directry) as f:
            lines = f.readlines()
        count = 0 #
        for line in lines: #
            count += 1
            print(line)

    def function1_1():
        session = InstaPy(username = user_ins, password = user_pas)
        session.login()

def main():
    loading(3,"Loading")
    check_logs()
    loading(6,"Opening bot")

main()