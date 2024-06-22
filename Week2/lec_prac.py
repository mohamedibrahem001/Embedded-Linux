#!/usr/bin/python3
# file  : lec_prac.py
# author : Mohamed Ibrahem (mohamed.ibrahem2608@gmail.com)
# brief  : 
#   this file to practise pyton     
# version : 0.1
# date    : 2024-06-15
# copyright Copyright (c) 2024


#break tuples 
"""fruits= ("apple","banana","cheery","orange","kiwi")
(green,yellow,*red)=fruits

print(green,yellow,red)
print(type(red))
(green,*tropic,red)=fruits
print(green,tropic,red)"""

#join tuples
"""
tuple1 =('a','b','c')
tuple2 = ('1','2',3,'2')
tuple3=tuple1+tuple2

print(tuple3)
print(tuple3.count('2'))
print(tuple3.index('2'))"""
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
#pyautoGui
import pyautogui
from time import sleep
"""
sleep(3)
try: 
    location=None
    while location is None:
        location =pyautogui.locateOnScreen('play.png')     
        sleep(1)
    pyautogui.moveTo(location.left,location.top)    

except pyautogui.ImageNotFoundException:
        print("image not found ...")
       # exit()
"""
sleep(3)
pyautogui.write("hello world")

#pyautogui.click(location.left+10,location.top +30)

  



