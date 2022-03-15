# from .func1_ import *
#Installing Tool's settings
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

print("test message")

def check_logs():
    if os.path.isdir('logs') == True:
        pass
    else: #
        os.mkdir("logs")