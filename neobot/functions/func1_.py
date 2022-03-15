from instapy import InstaPy
import random
from PIL import Image
import time
import sys
import os
from main import user_ins, user_pas, cookiesfile

class function1():
    def __init__(self): 
        pass
    
directry = str(cookiesfile+".txt")
lines = []
with open(directry) as f:
    lines = f.readlines()

count = 0 #
for line in lines: #
    count += 1
    print(line)

def main():
    session = InstaPy(username = user_ins, password = user_pas)
    session.login()