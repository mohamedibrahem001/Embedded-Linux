#!/usr/bin/python3
# file  : lec_prac.py
# author : Mohamed Ibrahem (mohamed.ibrahem2608@gmail.com)
# brief  : 
#   this file to practise pyton     
# version : 0.1
# date    : 2024-06-24
# copyright Copyright (c) 2024

#---------------------------------------------
#classes
#inhertance
#
#class animle:
#    def __init__(self):
#        print("constructor is called")
#        
#    def eat(self):
#        print("eat food")
#    def __del__(self):
#        print("destructor is called")
#
#class cat(animle):
#    def __init__(self):
#        print("child constructor is called ")
#        super().__init__()
#    def sound(self):
#        print("meaouuu")
#    def __del__(self):
#      print("child destructor is called")
#      super().__del__()
#
#my_cat= cat()
#my_cat.eat()
#my_cat.sound()
#print("End of the Program")
#
#---------------------------------------------
##class members 
#class Base: 
#    def __init__(self):
#        self.a ="public member"
#        self.__c="private member"
#    def privatefunc (self):
#        return self.__c
#    def __pri_func():
#        print("from privte func")
#
#class Derived(Base):
#    def init(self):
#        #calling constructor of the base calls
#        super().__init__(self)
#
#obj  = Base()
#print(obj.a)
#
#print(obj.privatefunc())    
#print(obj._Base__c)
#        
#print(obj._Base__pri_func())
#---------------------------------------------
#static method 

#---------------------------------------------
#overload + operator 
#class point:
#    def __init__(self,x_coord=0,y_coord=0):
#        self.x_coord=x_coord
#        self.y_coord=y_coord
#    #overload + operator
#    def __add__ (self,point_o):
#        return (point(self.x_coord+point_o.x_coord,self.y_coord+point_o.y_coord))
#    
#point1 = point(2,4)
#point2 = point(3,7)
#print("point1.x =  " +str(point1.x_coord))
#print("point1. =  " +str(point1.y_coord))
#
#print("point2.x =  " +str(point2.x_coord))
#print("point2.y =  " +str(point2.y_coord))
#
#point3= point1+point2
#print("point3.x =  " +str(point3.x_coord))
#print("point3.y =  " +str(point3.y_coord))

#---------------------------------------------
#files
# 'a' to append to the last location in the file 
# 'r' for read only from the file 
# 'w' to start new file and write from the start 

#f = open("test.txt",'a')
##f.write("hello this is a demo typing ")
#f.write("Good Evening . \n")
#f.close()
#f = open("test.txt")
#print(f.read())
#f.close()

#with open("test.txt") as f:
#    print(f.read())
#--------------------------------
# count number of lines 
#f =open("test.txt",'r')   
#ls =f.readlines()     #read and append in a list
#print(len(ls)) #find the length of the list
#
## count number of words 
#f =open("test.txt",'r')   
#stri =f.read()
#ls = stri.split() # divid the whole string into a list of sub strings 
#print(len(ls)) #find the length of the list
#--------------------------------
# append a list to a file 
#lst =[' ahmed','mahmoud','ibrahem ']
#with open("test.txt",'a') as fs:
#   fs.write(" ".join(lst))
#--------------------------------
#handle csv file  
#write a  list of dictiories
#import os
#import csv 
#data =[{"name":"mohamed ibrahem",
#    "age":30,
#    "Job":"engineer"},
# {   "name":"hassan ibrahem",
#    "age":40,
#    "Job":"teacher"}]
#
#
#filenm ="log1.csv"
#file_exist =os.path.isfile(filenm)
#
#with open(filenm,'a') as f:
#    writer=csv.DictWriter(f,fieldnames=data[0].keys())
#    if not file_exist:
#      
#        writer.writeheader()
#
#    for li in range (len(data)) :
#        #writer=csv.DictWriter(f,fieldnames=data.keys())
#        writer.writerow(data[li])
#   
#--------------------------------
#handle csv file  
#read from csv
#import os
#import csv 
#
#fd = open("log1.csv",'r')
#
#reader= csv.reader(fd)
#for row in reader:
#    print(row)
#    
#--------------------------------
#handle excel sheets 
#import openpyxl
#filename='test_excel.xlsx'
#wb=openpyxl.load_workbook(filename)
#print(wb)

#Reading from excel :===========

#for  row in wb['Sheet2'].iter_rows(values_only=True):
#    print(row)

#Writing to excel :===========

#data = [['alice',6666],
#        ['Bob',999999999999],
#        ['charlie',33]
#        ]
#for row in data:
#    wb.active.append(row)
#wb.save(filename)
#wb.close()

#Creating new sheet :===========

#new_sheet=wb.create_sheet(title="Tasks")
#new_sheet["A1"]="Task Name"
#new_sheet["B1"]="Priority"
#new_sheet["C1"]="Due Date"
#new_sheet["D1"]="Notes"h
#wb.save(filename)
#wb.close()
#pandas with files
#import pandas as pd
#def read_csv(file_path):
#    return pd.read_csv(file_path)
#def read_excel(file_path):
#    return pd.read_excel(file_path)
#print(read_excel("test_excel.xlsx"))
#print("-"*60)
#print(read_csv("log1.csv"))
#--------------------------------
#threading: 
#
#import threading 
#import os
#from time import sleep
#
#def task1(): 
#   while True:
#      print("task1 is assigned to {}".format(threading.current_thread().name)) 
#      print("task1 Id of the running process is {}".format(os.getpid()))
#      sleep(.1)
#
#def task2(): 
#   while True:
#      print("task2 is assigned to {}".format(threading.current_thread().name)) 
#      print("task2 Id of the running process is {}".format(os.getpid()))
#      sleep(.1)
#
#t1 = threading.Thread(target=task1).start() #thread 1 creation 
#t2 = threading.Thread(target=task2).start() #thread 2 creation
##main thread
#while True: 
#    print("main thread ")
#    sleep(.1)   
#---------------------------------------------------------
# sockets: 
#---------------------------------------------------------
#gui: 
#import tkinter
#root= tkinter.Tk()
#root.title("Calculator")
#root.geometry("400x400+250+300")
#root.resizable(0,0)
#root.configure(background="#00CCbb")
#tkinter.Label(root,text="Num 1 ",fg="#FF0000").pack(pady=10)
#tkinter.Label(root,text="Num 2 ",fg="#00FF00").pack(pady=50)
#tkinter.Label(root,text="Num 3 ",fg="#0000FF").pack(pady=110)
#root.mainloop()

#from customtkinter import *
#
#root=CTk()
#root.title("Calculator")
#set_appearance_mode("dark")
#root.geometry("400x400+250+300")
#root.resizable(0,0)
#root.mainloop()

#from  tkinter import *
#root= Tk()
#root.title("Calculator")
#root.geometry("400x400+450+300")
##root.resizable(0,0)
##root.configure(background="#00CCbb")
#frame=Frame(root,background="yellow")
#frame.pack(expand=TRUE,fill="both",side="left")
#val= StringVar()
#entry =Entry(frame,font=("Arail",20,"bold"),textvariable=val)
#entry.pack(side="right")
#label=Label(frame,text="Name",fg="yellow",background="black"    )
#label.pack(side="left")
#
#
#val2= StringVar()
#def btn_handler():
#    print(f"{val.get()}")
#    val.set("")
#
#entry2 =Entry(frame,font=("Arail",20,"bold"),textvariable=val)
#entry2.pack(side="right")
#label2=Label(frame,text="Password",fg="yellow",background="black")
#label2.pack(side="left",pady=30)
#btn =Button(frame,text="click here",font=("Arail",11),command=btn_handler)
#btn.pack(side="bottom")
#
# 
##frame2=Frame(root,background="green")
##frame2.pack(expand=TRUE,fill="both",side="right")
##
##label2= Label(frame2,text="Num 2 ",fg="green",background="black")
###Label(root,text="Num 3 ",fg="#0000FF").pack(pady=110)
##label2.pack()
#
#root.mainloop()
##########################################################################3
#login screen
"""
from  tkinter import *
root= Tk()
root.title("Calculator")
root.geometry("400x400+450+300")
 
frame=Frame(root)
frame.pack(expand=TRUE,fill="both",side="left")

val_name= StringVar()
val_password= StringVar()
 
def btn_handler():
    print(f"user name ={val_name.get()}")
    print(f"user password ={val_password.get()}")
    val_name.set("")
    val_password.set("")

def group_lbl_entry(value,mytext):
    global frame
    label_name=Label(frame,text=mytext)
    entry =Entry(frame,font=("Arail",20,"bold"),textvariable=value)
    return entry,label_name


#label_name=Label(frame,text="Name",fg="yellow",background="black"    )
#label_name.pack( )
#entry =Entry(frame,font=("Arail",20,"bold"),textvariable=val_name)
#entry.pack()

#label2=Label(frame,text="Password",fg="yellow",background="black")
#label2.pack( )
#entry2 =Entry(frame,font=("Arail",20,"bold"),textvariable=val_password)
#entry2.pack()

entry1,lable1=group_lbl_entry(val_name,"Name")
entry1.grid(row=0,column=1)
lable1.grid(row=0,column=0)

entry2,lable2=group_lbl_entry(val_password,"Password")
entry2.grid(row=1,column=1)
lable2.grid(row=1,column=0)

btn =Button(frame,text="click here",font=("Arail",11),command=btn_handler)
btn.grid(row=2,column=1)

 
#frame2=Frame(root,background="green")
#frame2.pack(expand=TRUE,fill="both",side="right")
#
#label2= Label(frame2,text="Num 2 ",fg="green",background="black")
#Label(root,text="Num 3 ",fg="#0000FF").pack(pady=110)
#label2.pack()

mainloop()
"""
########################################################
#List Box
#from  tkinter import *
#import os 
#def items_selected(event):
#    selected_index= lb.get(lb.curselection())
#    print(f"selected : {selected_index}")
#    if selected_index == 'c':
#        os.system("ls -l ") #it writes in cmd line 
#   # print(lb.get(lb.curselection()))
#
#top =Tk()
#lb =Listbox(top)
#lb.insert(1,"python")
#lb.insert(2,"java")
#lb.insert(3,"c")
#lb.insert(4,"c++")
#lb.pack()
#lb.bind('<<ListboxSelect>>',items_selected)
#
#mainloop()

#from tkinter import *
#import os
#root =Tk()
#root.title("simple app")
#root.geometry("400x400+450+300")
#val=IntVar()
#rd1=Radiobutton(root,text="python",value=1,variable=val)
#rd1.grid(row=0,column=0)
#rd2=Radiobutton(root,text="java  ",value=2,variable=val)
#rd2.grid(row=1,column=0)
#btn = Button(root,text='click here',command=lambda:print(val.get()))
#btn.grid(row=2)
#
#root.mainloop()
##########################################################################
### RadioButton and scale
#from tkinter import *
#import threading 
#import timer
#
#root =Tk()
#val = IntVar()
#Radiobutton(root,text="APP1 ",variable=val,value=1).pack(anchor=W)
#Radiobutton(root,text="APP2 ",variable=val,value=2).pack(anchor=W)
#Radiobutton(root,text="None ",variable=val,value=3).pack(anchor=W)
#def show():
#    global t
#    print(val.get())
#    if val.get() == 1:
#        print("app1")
#    elif(val.get()==2):
#        print("app2")
#    else :
#        print("none")
#    t =threading.Timer(.1,show)
#    t.start()
#
#Scale(root,from_=0,to=300,orient=HORIZONTAL,variable=val).pack()
#
#threading.Timer(1,show).start()
#
#try:
#    root.mainloop()
#    t.cancel()
#except:
#    print("Exit")
#    exit()
#
#
##################################################3
## Widgets
#from tkinter import *
#import threading
#parent_widget =Tk()
#txt_widget =Text(parent_widget,width=20,height=3)
#txt_widget.insert(END,"Hello from egypt  ")
#txt_widget.insert(END,"ibrahem")
#txt_widget.pack()
#val =StringVar()
#def show():
#    global t
#    print(txt_widget.get("1.0",END))
#    
#    t =threading.Timer(1,show)
#    t.start()
##
##Scale(root,from_=0,to=300,orient=HORIZONTAL,variable=val).pack()
##
#threading.Timer(1,show).start()
#
#mainloop()
##################################################################
#NewFrom : 1:17:22
#
#from tkinter import * 
#
#
#root =Tk()
#root.title("simple app")
#root.geometry("400x400+450+300")
#val=StringVar()
#def open_new_window():
#    new_window =Toplevel(root)
#    new_window.title("new window")
#    new_window.geometry("200x200")
#    Label1=Label(new_window,text="Hello ........ ")
#    Label1.pack()
#    new_window.mainloop()
#
#btn = Button(root,text="sub wind",command=open_new_window)
#
#btn.pack()
#mainloop()
#import os
#os.environ["QT_QPA_PLATFORM"] = "xcb"
#import cv2
#
#def main():
#    #create a video capture object
#    cap=cv2.VideoCapture(0)
#    if not cap.isOpened():
#        print("can't open webcam")
#        exit()
#    while True:
#        #capture frame by frame
#        ret,frame=cap.read()
#        if not ret:
#            print("can't receive frame")
#            break
#        #show the frame
#        cv2.imshow("frame",frame)
#        #wait for 100 miliseconds
#        if cv2.waitKey(100) & 0xFF == ord('q'):
#           
#            break 
#    cap.release()
#    cv2.destroyAllWindows()
#
#main()
################################################
## capture image 
#import os
#os.environ["QT_QPA_PLATFORM"] = "xcb"
#import cv2
#
#def main():
#    #create a video capture object
#    cap=cv2.VideoCapture(0)
#    if not cap.isOpened():
#        print("can't open webcam")
#        exit()
#    while True:
#        #capture frame by frame
#        ret,frame=cap.read()
#        if not ret:
#            print("can't receive frame")
#            break
#        #show the frame
#        cv2.imshow("frame",frame)
#        key =cv2.waitKey(100)
#        #wait for 100 miliseconds
#        if key & 0xFF == ord('q'):
#            break 
#        if key & 0xFF == ord('c'):
#            cv2.imwrite('im.jpg',frame) 
#    cap.release()
#    cv2.destroyAllWindows()
#
#main()
################################################
## promptopen 

#import os
#out= os.popen("ls")
#ls=out.read()
#print(ls)
#print(type(ls))
#ls=ls.split()
##ls =list(ls)
#print(ls)
#print(type(ls))
#os.popen(f"code {ls[2]}")
###################################################
#flask 
from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/greet/<name>')
def greet_p(name):
    return (f"Hello ,{name}!")

if __name__ == '__main__':
    app.run()
#################
#2.10.00