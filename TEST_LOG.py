# # import time
# # import sys

# # for remaining in range(3, 0, -1):
# #     sys.stdout.write("\r")
# #     sys.stdout.write("{:2d} seconds remaining.".format(remaining)) 
# #     sys.stdout.flush()
# #     time.sleep(1)

# # sys.stdout.write("\rTerminal closed            \n")
# import keyboard

# selected = 1

# def show_menu():
#     global selected
#     print("\n" * 30)
#     print("Choose an option:")
#     for i in range(1, 5):
#         print("{1} {0}. Do something {0} {2}".format(i, ">" if selected == i else " ", "<" if selected == i else " "))

# def up():
#     global selected
#     if selected == 1:
#         return
#     selected -= 1
#     show_menu()

# def down():
#     global selected
#     if selected == 4:
#         return
#     selected += 1
#     show_menu()

# show_menu()
# keyboard.add_hotkey('up', up)
# keyboard.add_hotkey('down', down)
# keyboard.wait()

# # import enquiries

# # options = ['Do Something 1', 'Do Something 2', 'Do Something 3']
# # choice = enquiries.choose('Choose one of these options: ', options)

# # print(choice)

# # from pick import pick

# # title = 'Please choose your favorite programming language: '
# # options = ['Java', 'JavaScript', 'Python', 'PHP', 'C++', 'Erlang', 'Haskell']

# # option, index = pick(options, title, indicator='--', default_index=2)
# import math
# print(1.08678*(10.0**12.0))

# import subprocess

# subprocess.call("C:/Users/PetesHacker/AppData/Local/Programs/Hyper")

# stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT

# from tqdm import tqdm
# import time
# import random

# for i in tqdm(range(random.randint(1, 20))):
#     time.sleep(random.uniform(0.1 ,0.9))


# import getpass
  
# pwd = getpass.getpass()
# print("You entered: ", pwd)

# import msvcrt
# import getch

# def getPass():
#     passwor = ''
#     while True:
#         x = getch.getch()
#         # x = msvcrt.getch().decode("utf-8")
#         if x == '\r' or x == '\n':
#             break
#         print('*', end='', flush=True)
#         passwor +=x
#     return passwor

# print("\nout=", getPass())
# import os
# import sys
# import subprocess
# print subprocess.Popen("echo Hello World", shell=True, stdout=subprocess.PIPE).stdout.read()
import urllib.request
import time
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()
   with open("test.txt",'w') as test:
       test.write(str(html))
