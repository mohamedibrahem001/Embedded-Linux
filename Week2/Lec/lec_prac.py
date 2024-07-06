#!/usr/bin/python3
# file  : lec_prac.py
# author : Mohamed Ibrahem (mohamed.ibrahem2608@gmail.com)
# brief  : 
#   this file to practise pyton     
# version : 0.1
# date    : 2024-06-15
# copyright Copyright (c) 2024

#---------------------------------------------
#break tuples 
"""fruits= ("apple","banana","cheery","orange","kiwi")
(green,yellow,*red)=fruits

print(green,yellow,red)
print(type(red))
(green,*tropic,red)=fruits
print(green,tropic,red)"""
#---------------------------------------------
#join tuples
"""
tuple1 =('a','b','c')
tuple2 = ('1','2',3,'2')
tuple3=tuple1+tuple2

print(tuple3)
print(tuple3.count('2'))
print(tuple3.index('2'))"""
#---------------------------------------------
#sets
"""sets ={"hello","mohamed","bek"}
print(sets)
print(sets.add("hello2"))
print("length of the set : "+str(len(sets)))
print(sets)
sets.pop()
print(sets)
sets2={"hello","ahmed","bek"}           
print(sets.intersection(sets2))
"""

#---------------------------------------------
#pyautoGui
#import pyautogui
#import keyboard
#from time import sleep
#pyautogui.FAILSAFE = True
#sleep(2)
#
#while True:
#    print(pyautogui.position())
#    sleep(0.2)

#pyautogui.hotkey('win')


# Press the left Windows key
#keyboard.press_and_release('win')
#pyautogui.typewrite('terminato')
#sleep(2)
#pyautogui.PAUSE=0.25
#print(pyautogui.KEYBOARD_KEYS)
#

#
#sleep(3)
#pyautogui.hotkey('shift','right')
#sleep(1)
#pyautogui.hotkey('shift','right')
#sleep(1)
#pyautogui.hotkey('shift','right')
#sleep(1)
#pyautogui.hotkey('shift','right')
#sleep(1)
#

#pyautogui.moveTo(100,100,duration=1)
#sleep(2)


#try: 
#    location=None
#    while location is None:
#       # location =pyautogui.locateOnScreen('/home/mohamed-ibrahem/Desktop/EmbeddedLinux/Embedded-Linux/Week2/play.png',confidence=0.9)
#       #location =pyautogui.locateCenterOnScreen('/home/mohamed-ibrahem/Desktop/EmbeddedLinux/Embedded-Linux/Week2/play1.png',confidence=0.9) 
#        location =pyautogui.locateCenterOnScreen('extensions.png',confidence=0.7)     
#        sleep(1)
#    pyautogui.click(location)     
#except pyautogui.ImageNotFoundException:
#        print("image not found ...")
#        exit()



#pyautogui.moveTo(20,20)   

#pyautogui.click(location.left+10,location.top +30)
#---------------------------------------------
#BeautifulSoup
#import csv
#from bs4 import BeautifulSoup
#
 
  
#---------------------------------------------
#date time 
#import datetime 
#print(datetime.datetime.now().strftime('%Y.%m.%d %H:%M:%S')) # to be used while logging 
#---------------------------------------------
#math modules
#import math
#ls =[1,2,3,4,5,6]
#print(min(ls))
#print(max(ls))
#---------------------------------------------
#classes
#class Person:
#    def __init__(self,name):#constructor
#        self.name =name
#        print(f"{name} has been created ")
#
#    def __del__ (self):#destructor
#        print(f"{self.name} has been deleted ")
#    
#    def change_name(self,name):
#        self.name = name
#        print(f"name has been changed to {self.name}") 
#p=Person("mohamed")
#p2=Person("ibrahem")
#del (p)
#p2.change_name("hassan")
#print("End of The Program")