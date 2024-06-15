#!/usr/bin/python3

# file  : fav_websites.py
# author : Mohamed Ibrahem (mohamed.ibrahem2608@gmail.com)
# brief  : 
#   this file to help you to access web directly     
# version : 0.1
# date    : 2024-06-15
# copyright Copyright (c) 2024


import webbrowser 

def fireWebsites(x):
    if 1==x:
        print("your selection is Google")
        webbrowser.open("WWW.google.com")
    elif 2==x:
        print("your selection is linkedin")
        webbrowser.open("WWW.linkedin.com")
    elif 3==x:
         print("your selection is youtube")
         webbrowser.open("WWW.youtube.com")
    elif 4==x:
         print("your selection is youtube")
         webbrowser.open("WWW.facebook.com")



def firefox_fav_taps():
    ch=int(input("1.Google\n2.Linkedin\n3.youtube\n4.facebook"))
    fireWebsites(ch)