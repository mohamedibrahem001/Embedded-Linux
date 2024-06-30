#!/usr/bin/python3
# file  : alexa.py
# author : Mohamed Ibrahem (mohamed.ibrahem2608@gmail.com)
# brief  : 
#  basic implementation of alexa a voice recognition app 
# version : 0.1
# date    : 2024-06-27
# copyright Copyright (c) 2024

#--------------------------------------------

import os   #to handle operating system operations
import time #to handle time operations
import datetime #to get dta and time 
import webbrowser #to handle browsing operations 
import speech_recognition as sr# to handle speech commands 
from gtts import gTTS  # goodle pack to handle text to speach
import playsound # to play sound 
import requests # to handle web requests 
class alexa:
    alexa_language="" #alexa languuage 
    def __init__(self,alexa_lang):
         
         self.alexa_language=alexa_lang
      
    def lookfor_cmd(self,lis,cmd):
        for i in lis:
            if i in cmd:
                return True
        return False
    def speak(self,data,language):
        output = gTTS(text=data,lang=language,slow=True)
        output.save("output.mp3")
        playsound.playsound("output.mp3")
        os.remove("output.mp3")
    
    def read(self):
        # Create a Recognizer instance
        recognizer = sr.Recognizer()
        mic = sr.Microphone()
        with mic as source:
            print("Listening for your command...")
            audio = recognizer.listen(source)
            try:
                if self.alexa_language == 'ar':   
                   command = recognizer.recognize_google(audio, language='ar')
                elif self.alexa_language == 'en':
                    command = recognizer.recognize_google(audio, language='en')
                print(f"You said: {command}")
                command = command.lower()
                return command
            except sr.UnknownValueError:
                print("Sorry, I could not understand your command.")
                self.speak
                return ""
            except sr.RequestError:
                print("Could not request results from Google Speech Recognition service.")
                return ""
    def weather_now(self):
        api_key = "4f7762ffedebc4d5a6b94dd6241f4863"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = "Cairo"
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
        
        data = requests.get(str(complete_url)).json()
        #print(data)
        if data["cod"] != "404":
            main = data["main"]
            weather = data["weather"][0]
            temperature = main["temp"]
            temperature =int(temperature) - 273
            if self.alexa_language == 'en':
                weather_report = f"The current temperature is {temperature} degrees Celsius."
                self.speak(weather_report, 'en')
            else:
                weather_report = f"درجة الحرارة الحالية هي {temperature} درجة مئوية  ."
                self.speak(weather_report, 'ar')
        else:
            if self.alexa_language == 'en':
                self.speak("City not found.", 'en')
            else:
                self.speak("لم يتم العثور على المدينة.", 'ar')
    def process(self):
        cmd_txt =self.read()
        time_list =['time','الساعه' ,'ساعه','الوقت','وقت']
        date_list =['date','تاريخ','التاريخ','اليوم' ]
        face_book= ['facebook','الفيسبوك','فيسبوك']
        you_tube= ['youtube','اليوتيوب','يوتيوب']
        google= ['google','جوجل']
        weather= ['weather','temperature','الطقس','طقس','درجة الحرارة']
        exit_ls= ['exit','terminate','خروج','انهاء']

        if self.lookfor_cmd(lis=time_list,cmd=cmd_txt):
            self.time_now()
        elif self.lookfor_cmd(lis=date_list,cmd=cmd_txt):
            self.date_now()
        elif self.lookfor_cmd(lis=face_book,cmd=cmd_txt):
            webbrowser.open('https://www.facebook.com/')
        elif self.lookfor_cmd(lis=you_tube,cmd=cmd_txt):
            webbrowser.open('https://www.youtube.com/')
        elif self.lookfor_cmd(lis=google,cmd=cmd_txt):
            webbrowser.open('https://www.google.com/')
        elif self.lookfor_cmd(lis=weather,cmd=cmd_txt):
            self.weather_now()
        elif self.lookfor_cmd(lis=exit_ls,cmd=cmd_txt):
                global loop
                loop =False
        
    def time_now(self):
        if self.alexa_language == 'en':
            current_time = "Time now is "+str(datetime.datetime.now().strftime("%H:%M:%S"))
            self.speak(current_time,'en')
        else:
            current_time = "الساعة الآن  :"+str(datetime.datetime.now().strftime("%H:%M:%S"))
            self.speak(current_time,'ar')
       
    def date_now(self):
        if self.alexa_language == 'en':
            current_date = "Date now is "+str(datetime.datetime.now().strftime("%Y-%m-%d"))
            self.speak(current_date,'en')
        else:
            current_date = "التاريخ الآن  :"+str(datetime.datetime.now().strftime("%Y-%m-%d"))
            self.speak(current_date,'ar') 

    def __del__(self):
       pass


hanadi =alexa('ar')

#print(sr.Microphone.list_microphone_names())
 
loop=True

while loop:
    hanadi.process()
    time.sleep(0.1)


 