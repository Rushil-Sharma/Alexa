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
Jarvis = pyt.init()
def Quit():
    Jarvis.say("For saftey we will clear the screen")
    Jarvis.runAndWait()
    os.system('clear')
    sys.exit(0)
def Change_voice():
    voices = Jarvis.getProperty('voices')
    if x%2 == 0:
        Jarvis.setProperty('voice', voices[1].id)
    elif x%2 != 0:
        Jarvis.setProperty('voice', voices[0].id)
    x=x+1  
def Q_a():
    if d%2 == 0:
        Jarvis.say("I have no clue")
        Jarvis.runAndWait()
        print("No clue")
    elif d%3 == 0:
        Jarvis.say("Sorry i can not do that")
        Jarvis.runAndWait()
        print("Sorry i can not do that")
    elif d%5 == 0:
        Jarvis.say("i am amazed can you do that for me ?")
        Jarvis.runAndWait()
        print("i am amazed can you do that for me ?")
    else:
        Jarvis.say("I have no answer to that question ")
        Jarvis.runAndWait()
        print("I have no answer to that question")
    d=d+1
