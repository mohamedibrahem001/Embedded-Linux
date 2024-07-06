#!/usr/bin/python3
# file  : lec_prac.py
# author : Mohamed Ibrahem (mohamed.ibrahem2608@gmail.com)
# brief  : 
#   this file to  solve python task      
# version : 0.1
# date    : 2024-06-25
# copyright Copyright (c) 2024

#--------------------------------------------
#doxgen/ header parser and set unique id for each function 
import os
from bs4 import BeautifulSoup
import openpyxl
# html file path is : /home/mohamed-ibrahem/Desktop/EmbeddedLinux/Embedded-Linux/Week3/Tasks/c_module/docs/html

parse_dir =input("enter path to the HTML directory: ")
print("current directory: is      "+ str(os.getcwd()))
os.chdir("".join(parse_dir))
print("current directory: is      "+ str(os.getcwd()))