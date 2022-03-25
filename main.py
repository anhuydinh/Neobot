import functions
from instapy import InstaPy
import random
from PIL import Image
import time
import sys
import subprocess
import string
import os
import curses
# from functions.func1_ import readCookies
# from functions import function1

# from getpass import getpass
# from func1 import *

#---------Setup




#-----------Quick turn off
    

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
color_random=[bcolors.HEADER,bcolors.OKBLUE,bcolors.OKCYAN,bcolors.OKGREEN,bcolors.WARNING,bcolors.FAIL,bcolors.UNDERLINE]
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
                                            https://github.com/PeterBenj2000/Neobot
                                                     PROTOTYPE VER
"""+ bcolors.ENDC
tab1 = " " * 32
# time.sleep(10)

print(interf1)  

# def cookiesa():
#     print(bcolors.FAIL+ "This program uses cookies!!!!"+bcolors.ENDC)

#     time.sleep(2)
#     functions.clear_scr()


#Functions 
functions_menu = bcolors.WARNING+""" 
{1}--I automation 
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
print("logs generated: "+ cookiesfile)
#Generate custom cookie file

cookies_path = "logs/{path}.txt"
def genCookies(content):
    with open(cookies_path.format(path = str(cookiesfile)), 'w') as cookie:
        cookie.write(str(content))
        cookie.close()
    # time.sleep(5) #Test sleep

genCookies(cookiesfile+".txt")
# mainfunc1.readCookies()
# function1.readCookies()

# time.sleep(60)
#Clearing cookies file
def clear_cookies():
    cookiopn = open(cookies_path.format(path = str(cookiesfile)), 'w')
    cookiopn.close()

# clear_cookies()

#------------------------------------------------------------------
time.sleep(1) #Let them see the title first lol
print(functions_menu)
time.sleep(1)
breakloop = False

#Handling functions
def handle1(): #Instabot 
    functions.loading(10,"Initiating Function 1: ")
    functions.clear_scr()
    global breakloop
    global user_ins
    global user_pas
    print(bcolors.WARNING+ "Function 1 selected \n"+bcolors.ENDC)
    user_ins = input("Enter instagram username: ") 
    user_pas = input( "Enter password instagram password: ")
    functions.clear_scr()
    #---------Generating password cookies----------
    
    genCookies(content = user_ins+"\n"+user_pas)
    # subprocess.call("C:/Users/PetesHacker/Desktop/Folders/Code/Python/Custom project/neobot/func1_.py")
    
    #--------clearing cookies------------
    # time.sleep(10) #Test for clearing

    # loginn()
    #bot()
    functions.clear_scr()
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
        breakloop = True
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
    for remaining in range(2, 0, -1):
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
