from instapy import InstaPy
import random
from PIL import Image
import time
import sys
import subprocess
import string
# import keyboard #Turns on to activate quickly turn off function (Broken btw)
import os
import functions
# from getpass import getpass
# from func1 import *

#---------Setup
def clear_scr():
    os.system("clear")

clear_scr()

# if os.path.isdir('logs') == True:
#     pass
# else: #
#     os.mkdir("logs")

functions.check_logs()
#Quickly turn off
    
# def check1():
#     if keyboard.read_key() == "F12":
#         print("Console closed")
#     else:
#         pass
# check1()

#Colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Greetings/Interface
color_random=[bcolors.HEADER,bcolors.OKBLUE,bcolors.OKCYAN,bcolors.OKGREEN,bcolors.WARNING,bcolors.FAIL,bcolors.BOLD,bcolors.UNDERLINE]
random.shuffle(color_random)
interf1 = color_random[0] +"""
                                # /$$   /$$                     /$$                   /$$    
                                # | $$$ | $$                    | $$                  | $$    
                                # | $$$$| $$  /$$$$$$   /$$$$$$ | $$$$$$$   /$$$$$$  /$$$$$$  
                                # | $$ $$ $$ /$$__  $$ /$$__  $$| $$__  $$ /$$__  $$|_  $$_/  
                                # | $$  $$$$| $$$$$$$$| $$  \ $$| $$  \ $$| $$  \ $$  | $$    
                                # | $$\  $$$| $$_____/| $$  | $$| $$  | $$| $$  | $$  | $$ /$$
                                # | $$ \  $$|  $$$$$$$|  $$$$$$/| $$$$$$$/|  $$$$$$/  |  $$$$/
                                # |__/  \__/ \_______/ \______/ |_______/  \______/    \___/  
                             
                                }--------------{+} Coded By PetesHacker {+}--------------{
                                   }--------{+}  GitHub.com/PeterBenj2000 {+}--------{
                                              *read github des before using*
                                                     PROTOTYPE MODE
"""+ bcolors.ENDC
tab1 = " " * 32
print(interf1)  

def cookiesa():
    print(bcolors.FAIL+ "This program uses cookies!!!!"+bcolors.ENDC)

    time.sleep(2)
    clear_scr()


#Functions 
functions_menu = bcolors.WARNING+""" 
{1}--Instagram automation 
{2}--Spambot 
{3}--Autocomplete
{4}--Autowrite
{0}--End

--Note that this project is in heavy development
""" + bcolors.ENDC
#---------Create random names for cookies------------------------
digits1 = random.choices(string.digits, k=2)
letters1 = random.choices(string.ascii_uppercase, k=9)
sample = random.sample(digits1 + letters1, 11)
cookiesfile = "" + ''.join(sample)
print(cookiesfile)
#Generate custom cookie file
cookies_path = "logs/{path}.txt"
with open(cookies_path.format(path = str(cookiesfile)), 'w') as cookie:
    cookie.write(cookiesfile+".txt")

# time.sleep(5) #Test sleep
#Check if a cookies file exists


#Clearing cookies file
cookiopn = open(cookies_path.format(path = str(cookiesfile)), 'w')
cookiopn.close()
#------------------------------------------------------------------
time.sleep(1) #Let them see the title first lol
print(functions_menu)
time.sleep(1)
breakloop = False

#Handling functions
def handle1(): #Instabot 
    clear_scr()
    global breakloop
    global user_ins
    global user_pas
    print(bcolors.WARNING+ "Function 1 selected \n"+bcolors.ENDC)
    user_ins = input("Enter instagram username: ") 
    user_pas = input( "Enter password instagram password: ")
    #---------Generating password cookies----------
    file1 = open("passwordlog.txt", 'w')

    file1.write(str(user_ins))
    file1.write("\n" + str(user_pas))
    clear_scr()
    file1.close()
    # subprocess.call("C:/Users/PetesHacker/Desktop/Folders/Code/Python/Custom project/neobot/func1_.py")
    
    #--------clearing cookies------------
    time.sleep(10) #Test for clearing
    with open("passwordlog.txt",'w') as f1: #
        mess1 = ''
        f1.write(mess1)
    # loginn()
    #bot()
    clear_scr()
    print(bcolors.FAIL+ "Task completed successfully"+bcolors.ENDC)
    time.sleep(0.5)
    breakloop = True
    
def handle2(): #Spambot
    print(bcolors.WARNING+ "Function 2 selected \n"+bcolors.ENDC)
    return 0
def handle3(): #Auto
    print(bcolors.WARNING+ "Function 3 selected \n"+bcolors.ENDC)
    return 0
def handle4(): 
    print(bcolors.WARNING +"Function 4 selected \n"+bcolors.ENDC)
    return 0
def handle5(): #

    return 0
#while loop
while breakloop == False:
    selection = input("Select a function: ")

    if selection == "1":
        handle1()
        break
    elif selection == "2":
        handle2()
        break
    elif selection == "3":
        handle3()
        break
    elif selection == "4":
        handle4()
        break
    elif selection == "0":
        print(bcolors.WARNING+ "User chosed to exit program\n"+bcolors.ENDC)
        handle5()
    
    else:
        print("Error, retry")


def ClearCookies():
    print("Clear cookies?")
    os.system("rd /s \"logs\"")

ClearCookies()
# Exit code
# time.sleep(10) #Wait 10 secs to actually exit
def exit():
    for remaining in range(3, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("closing in {:2d}".format(remaining)) 
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\rTerminal closed            \n")

def out():
    exit1 = input("Enter to close terminal ")
    exit()

if breakloop == True:
    exit()

print("Program expired")