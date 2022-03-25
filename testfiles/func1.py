from instapy import InstaPy
import random
from PIL import Image
import time
import sys
import keyboard
import os
from main import user_ins
from main import user_pas

def loginn(): 
    
    session = InstaPy(username = user_ins, password = user_pas)
    session.login()

# class mainfunction(): 
#     def __init__(self,name,password):
#         self.name = user_ins
#         self.password = user_pas

#     def login(self,name,password):
#             session = InstaPy(username = name, password = password)
#             session.login()

# is there someone else or not?

