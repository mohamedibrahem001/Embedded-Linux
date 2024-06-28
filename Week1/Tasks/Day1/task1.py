#!/usr/bin/python3
# file  : task1.py
# author : Mohamed Ibrahem (mohamed.ibrahem2608@gmail.com)
# brief  : 
#   this file to solve python tasks     
# version : 0.1
# date    : 2024-06-14
# copyright Copyright (c) 2024


### 1. write a python program to count the number 4 in a given list
"""_summary_
this function to search for a number in a list.
"""
def check_existance(item_x, list_y):
    item_count = 0
    for item in range(len(list_y)):
        if list_y[item] == item_x:
            item_count = item_count +1 
    return item_count   


list_1 = [1,4,5,4,6,7,4]

print("count: "+str(check_existance(4,list_1)))
#print("count : "+ str(list_1.count(4) ))
print("--------------------------------")

### 2. write a python program to test whehter a passed letter is a vowel or not 

"""_summary_
        this  function to check if th passed character is vowel or not 
"""
def check_Vowel(c):
    ret_val =""
    vowels="aoiue"
    if (c.lower()) in vowels :
            ret_val = "Yes, Vowel"
    else:
            ret_val="No, It's not"
    return ret_val

ch =input("Is a vowel character:  ")
print(check_Vowel(ch))

print("--------------------------------")
### 3. write a python program to access environment variable using [PATH ] [os]

import os
"""
print(os.environ["HOME"])"""



# Get all environment variables
env_vars = os.environ

# Print all environment variables
for key, value in env_vars.items():
    print(f"{key}: {value}")
