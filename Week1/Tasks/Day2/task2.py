#!/usr/bin/python3
# file  : task2.py
# author : Mohamed Ibrahem (mohamed.ibrahem2608@gmail.com)
# brief  : 
#   this file to solve python tasks     
# version : 0.1
# date    : 2024-06-14
# copyright Copyright (c) 2024

#Task (4.2) : Get your public IP and get your location 
import requests

url = requests.get("https://api.ipify.org/?format=json")
ip=url.text
print("your global IP is : ")
print(ip)
ip=ip.removeprefix("{\"ip\":\"")
ip=ip.removesuffix("\"}")

print("your GEO coordinates is: ")

url = requests.get("https://ipinfo.io/"+(ip)+"/geo")
print(url.text)