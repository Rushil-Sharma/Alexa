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
import jarvis
import Usernames
k = 1
def main_code():
    joke=[
        """1 ...... What do you call a dinosaur that is sleeping? , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,
        A dino-snore!""",

        """2 ...... What is fast, loud and crunchy? , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,
        A rocket chip!""",

        """3 ...... Why did the teddy bear say no to dessert? , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,
        Because she was stuffed.""",

        """4 ...... What has ears but cannot hear? , ,  , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,
        A cornfield.""",

        """5 ...... What did the left eye say to the right eye? , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,
        Between us, something smells!""",

        """6 ...... What do you get when you cross a vampire and a snowman? , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,
        Frost bite!""",

        """7 ...... What did one plate say to the other plate? , ,  , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,
        Dinner is on me!""",

        """8 ...... Why did the student eat his homework? , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,
        Because the teacher told him it was a piece of cake!""",

        """9 ...... When you look for something, why is it always in the last place you look? , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,
        Because when you find it, you stop looking.""",

        """10 ...... What is brown, hairy and wears sunglasses? , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,
        A coconut on vacation."""
    ]
    riddles=[
        """1. Riddle: What has to be broken before you can use it?
        Answer: An egg""",

        """2. Riddle: I’m tall when I’m young, and I’m short when I’m old. What am I?
        Answer: A candle""",

        """3. Riddle: What month of the year has 28 days?
        Answer: All of them""",

        """4. Riddle: What is full of holes but still holds water?
        Answer: A sponge""",

        """5. Riddle: What question can you never answer yes to?
        Answer: Are you asleep yet?""",

        """6. Riddle: What is always in front of you but can’t be seen?
        Answer: The future""",

        """7. Riddle: There’s a one-story house in which everything is yellow. Yellow walls, yellow doors, yellow furniture. What color are the stairs?
        Answer: There aren’t any—it’s a one-story house.""",

        """8. Riddle. What can you break, even if you never pick it up or touch it?
        Answer: A promise""",

        """9. Riddle: What goes up but never comes down?
        Answer: Your age""",

        """10. Riddle: A man who was outside in the rain without an umbrella or hat didn’t get a single hair on his head wet. Why?
        Answer: He was bald."""
    ]
    Jarvis = pyt.init()
    Jarvis.say("Hello There How are you ? I am Jarvis what should i call you ?  ")
    Jarvis.runAndWait()
    def lolololol():
        operaton = input("type(+)or(-)or(*)or(/)) : ")
        first = int(input("First num: "))
        second = int(input("Second num: "))
        def plus():
            ans = int(first)+int(second)
            print("answer is",ans)
        def minus():
            ans = int(first)-int(second)
            print("answer is",ans)
        def mult():
            ans = int(first)*int(second)
            print("answer is",ans)
        def div():
            ans = int(first)/int(second)
            print("answer is",ans)
        if operaton == "+":
            plus()
        elif operaton == "-":
            minus()
        elif operaton == "*":
            mult()
        elif operaton == "/":
            if second != 0:
                div()
            else:
                print("0 division not possible")
        else:
            print()
    name = input("Can you please enter your name :  ")

    greet=("Hi",name)
    Jarvis.say(greet)
    Jarvis.runAndWait()
    Jarvis_name = 'Jarvis'
    x=d=0
    print("Enter A Command or type index<> for all the commands :")
    while True:
        if name == "no":
            ask_q = ("Enter a command : ")
        else:
            ask_q = (name,"Enter a command : ")
        Jarvis.say(ask_q)
        Jarvis.runAndWait()
        ans = input("<^-^> ")
        if 'quit' in ans:
            Command.Quit()
        elif 'hi' in ans or 'hey' in ans or 'hello' in ans or 'sup' in ans:
            print("hello i am",Jarvis_name)
            Jarvis.say('Hello')
            Jarvis.runAndWait()
        elif 'index<>' in ans:
            print("change your name - Default Jarvis \nchange my name - it will be asked in start \nclear<> - clear the screen \ngo to - Will search any thing on the internet \nplay song - will search it on youtube and give you the best result \nsearch - Will search on the net \nchange voice - will change the boy voice to girl - Defalt boy \ntime - will tell the time \nopen __ App will open the app math - this will do basic math for you \nit can also tell jokes and riddles")
        elif 'type<' in ans:
            if '>' in ans :
                ans = ans.replace("type<","")
                ans = ans.replace(">","")
                print(ans)
        elif 'change' in ans and 'name' in ans:
            if 'your' in ans:
                Jarvis_name = input("Enter a good name for me : ")
            elif 'my' in ans:
                name = input("Enter a good name for yourself : ")
        elif 'clear<>' in ans:
            Jarvis.say("Ok Clearing")
            Jarvis.runAndWait()        
            os.system('clear')
        elif 'speak' in ans:
            ans=ans.replace("speak ","")
            Jarvis.say(ans)
            Jarvis.runAndWait()
        elif 'go to' in ans:
            Command.Go_To()
        elif 'play' in ans and 'song' in ans:
            Command.Play_Song()
        elif 'search' in ans:
            Command.Search()
        elif 'change voice' in ans :
            voices = Jarvis.getProperty('voices')
            try:
                Jarvis.setProperty('voice', voices[1].id)
            except:
                Jarvis.setProperty('voice', voices[0].id) 
        elif 'time' in ans:
            time_now = time.strftime("%H:%M:%S")
            Jarvis.say(time_now)
            Jarvis.runAndWait()
        elif 'your name' in ans:
            J_n = ("I am",Jarvis_name,"You can also change my voice by the command : change your name and also change your name by the command : chsnge my name ")
            Jarvis.say(J_n)
            Jarvis.runAndWait()
        elif 'open youtube' in ans :
            webbrowser.open("youtube.com")
        elif 'open google' in ans :
            webbrowser.open("google.com")
        elif 'math' in ans:
            Jarvis.say("Ok Loading operators . . Compiling code . . Done !!! ")
            Jarvis.runAndWait()
            lolololol()
        elif '?' in ans :
            Command.Q_a()
        elif 'tell' in ans and 'joke' in ans:
            io = 1
            jokes = random.choice(joke)
            Jarvis.say(jokes)
            Jarvis.runAndWait()
        elif 'riddle' in ans:
            io = 1
            jokes = random.choice(riddles)
            Jarvis.say(jokes)
            Jarvis.runAndWait()
        elif 'image.open<' in ans and '>' in ans :
            Command.Image_Open()
        else:   
            print('INVALID')
