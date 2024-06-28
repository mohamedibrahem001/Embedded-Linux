#!/usr/bin/python3
# file  : task2.py
# author : Mohamed Ibrahem (mohamed.ibrahem2608@gmail.com)
# brief  : 
#   this file to solve python tasks     
# version : 0.1
# date    : 2024-06-14
# copyright Copyright (c) 2024


### write a python program which accepts teh radius of the circle
# from the user and compute the area of the circle 

def circle_area(rad):
    pi = 3.14159
    area = pi * radius **2
    return area


radius = float(input("enter the circle raduis: "))

print("area = "+ str(circle_area(radius)))
