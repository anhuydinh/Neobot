from instapy import InstaPy
import random
from PIL import Image
import time
import sys
import keyboard

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
interf1 = bcolors.FAIL +"""
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

"""+ bcolors.ENDC
tab1 = " " * 32
print(interf1)

#Functions 
functions_menu = bcolors.WARNING+""" 
{1}--Instagram automation #
{2}--Spambot #
{3}--Autocomplete
{4}--Autowrite

""" + bcolors.ENDC


time.sleep(1) #Let them see the title first lol
print(functions_menu)
time.sleep(1)
breakloop = False

#Handling functions
def handle1(): #Instabot 
    print(bcolors.WARNING+ "Function 1 selected \n"+bcolors.ENDC)
    user_ins = input("Enter instagram username: ") 
    user_pas = input("Enter password instagram password: ")
    # session = InstaPy(username = user_ins, password = user_pas)
    # session.login()
    #bot()
    
def handle2(): #Spambot
    print(bcolors.WARNING+ "Function 2 selected \n"+bcolors.ENDC)
    return 0
def handle3(): #Auto
    print(bcolors.WARNING+ "Function 3 selected \n"+bcolors.ENDC)
    return 0
def handle4(): 
    print(bcolors.WARNING +"Function 4 selected \n"+bcolors.ENDC)
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
    
    else:
        print("Error, retry")


# Exit code
time.sleep(10) #Wait 10 secs to actually exit
def exit():
    for remaining in range(3, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("closing in {:2d}".format(remaining)) 
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\rTerminal closed            \n")

exit1 = input("Enter to close terminal ")

exit()
sys.exit()