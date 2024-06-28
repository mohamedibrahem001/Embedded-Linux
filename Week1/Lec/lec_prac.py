#!/usr/bin/python3
"""def my_func(**arg):
    print(arg["name"])
    print(arg["age"])
    print(arg["mail"])


dic ={ "name":"mohamed ","age":"35","mail":"mohamed@gmail"}

my_func(**dic)
my_func(name="mostafa",age=36,mail="mosta@aaa")
"""

#variable global and local 
"""x= 555 
 
def func ():
    global x
    x = 111
    print(x)
    print(id(x))

func()
print(x)
print(id(x))"""

#lambda 
"""x =lambda a:a+10
print(x(5)) #15
print((lambda a:a+10)(5)) #15
"""

"""ls =[1,2,3,4,5, ]

print(list(map((lambda x:x*x),ls)))
"""
#modules
"""
import requests
from pprint import pprint
url = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
pprint(url.json())

"""

"""
from src.calc import sum

print(sum(5,6))
"""

#list
"""
list_x = [15,5,6,10,120,9]
list_x.sort()
print(list_x)
print("---------------------")
list_x.sort(reverse=True)
print(list_x)
"""

