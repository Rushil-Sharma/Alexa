from tkinter import *
from tkinter import messagebox
import pyttsx3 as pyt
import os
import sys 
from PIL import Image , ImageTk
import time 
import webbrowser
import wikipedia
import sqlite3
import random
import random
import smtplib
import Command
import pyttsx3 as pyt
import Alexa
s = ['let us go in my house','how does a bear run','better late than never','the train was late']
Jarvis = pyt.init()
Jarvis.say("Make sure it is you OK so this is a test to know whether you are a human or a robot listen carefully and type the sentence")
Jarvis.runAndWait()
asd = random.choice(s)
Jarvis.say(asd)
Jarvis.runAndWait()
r = input('Enter : ')
if r == asd:
    print('Correct')
else:
    print('wrong')
    sys.exit(0)
conn = sqlite3.connect('x.db')
c = conn.cursor()
c.execute('')
Jarvis.say("Hello There , . I will guide you in the email login process , Please wait till we load your screen . . . .")
Jarvis.runAndWait()
root = Tk()
root.title('Login.exe')
root.iconbitmap('lol.ico')
root.configure(bg='black')
canv = Canvas(root, width=80, height=80, bg='white')
canv.place(x = -200,y = 0)
Lbl1 = Label(root,text='Email :',font=('Helvatica',30))
Lbl1.grid(row=1,column=1)
Email = Entry(root,font=('Helvatica',50),bg='black',relief=FLAT,fg='light blue',show='^')
Email.grid(row=1,column=2)
def verification():    
    x = (Email.get())
    r = 0
    if '@gmail.com' in x:
        r=4
        sqliteConnection = sqlite3.connect('username.db')
        cursor = sqliteConnection.cursor()
        Jarvis.say("You are verified now close this screen for safety")
        Jarvis.runAndWait()
        root.mainloop()
        Alexa.main_code()
    else:
        messagebox.askokcancel('You might have entered the wrong email','email invalid')
Submit = Button(root,text='Submit',font=('Helvatica',30),fg='black',bg='gold',relief=FLAT,command=verification)
Submit.grid(row=3,column=1,columnspan=2)
Jarvis.say("Ok . . . now you can enter your email")
Jarvis.runAndWait()
root.mainloop()
