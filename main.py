from tkinter import *
import pyttsx3 as pyt
import os
import sys 
import time 
import webbrowser
import wikipedia
import random
import smtplib
import Command
import pyttsx3 as pyt
import Alexa
import Usernames
Jarvis = pyt.init()
Jarvis.say("Hello There , . I will guide you in the email login process , Please wait till we load your screen . . . .")
Jarvis.runAndWait()
root = Tk()
Lbl1 = Label(root,text='Email :',font=('Helvatica',30))
Lbl1.grid(row=1,column=1)
Email = Entry(root,font=('Helvatica',30))
Email.grid(row=1,column=2)
def verification():    
    x = (Email.get())
    r = 0
    if '@gmail.com' in x:
        r=4
    else:
        print('invalid  ')
    if r == 4:
        if x in Usernames.username :
            Jarvis.say("You are verified now close this screen for safety")
            Jarvis.runAndWait()
            root.mainloop()
            Alexa.main_code()
        else :
            asd = ("There are some limited usernames please try again")        
            Jarvis.say(asd)
            Jarvis.runAndWait()
Submit = Button(root,text='Submit',font=('Helvatica',30),fg='grey',bg='gold',command=verification)
Submit.grid(row=3,column=1,columnspan=2)
Jarvis.say("Ok . . . now you can enter your email")
Jarvis.runAndWait()
root.mainloop()
