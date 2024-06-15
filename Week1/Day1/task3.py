#!/usr/bin/python3
# file  : task3.py
# author : Mohamed Ibrahem (mohamed.ibrahem2608@gmail.com)
# brief  : 
#   this file to solve python tasks     
# version : 0.1
# date    : 2024-06-14
# copyright Copyright (c) 2024

### print the calendar  of the given month and year

import calendar 

year = int(input("enter a year : "))
mon =  int(input("enter a month: "))

print(calendar.month(year,mon))