#!/usr/bin/python3
# file  : task1.py
# author : Mohamed Ibrahem (mohamed.ibrahem2608@gmail.com)
# brief  : 
#   this file to use pyautogui module    
# version : 0.1
# date    : 2024-06-23
# copyright Copyright (c) 2024

#using pyautogui 
# 1. open vscode (ctrl + alt + t)
# 2. install clangd from extension
# 3. install c++ testmate from extension 
# 4. install c++ helper from extension
# 5. install cmake from extension
# 6. install cmake tools from extension
from pyautogui import *
import keyboard
from time import sleep
from PIL import ImageGrab, UnidentifiedImageError

#FAILSAFE = True
#
#try: 
#    location = None
#    while location is None:
#        location = locateCenterOnScreen('extensions.png', confidence=0.7)
#        print(location)
#        sleep(1)
#    click(location)
#except ImageNotFoundException:
#    print("Image not found ...")
#    exit()
#except UnidentifiedImageError:
#    print("Cannot identify image file ...")
#    exit()
#except Exception as e:
#    print(f"An error occurred: {e}")
#    exit()
#

res =locateOnScreen("search_icon.png")

print(res)
