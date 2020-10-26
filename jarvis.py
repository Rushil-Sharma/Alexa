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
import Usernames
history = []
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
        operaton = input("type(+)or(-)or(*)or(/)or(^)) : ")
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
        def power():
            ans = int(first)**nt(second)
            print("answer is",ans)            
        if operaton == "+":
            plus()
        elif operaton == "-":
            minus()
        elif operaton == "*":
            mult()
        elif operaton == "^":
            power()
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
        history.append(ans)
        if 'quit' in ans:
            Command.Quit()
        elif 'index<>' in ans:
            print("change your name - Default Jarvis \nchange my name - it will be asked in start \nclear<> - clear the screen \ngo to - Will search any thing on the internet \nplay song - will search it on youtube and give you the best result \nsearch - Will search on the net \nchange voice - will change the boy voice to girl - Defalt boy \ntime - will tell the time \nopen __ App will open the app math - this will do basic math for you \nit will store the users history\nit can also tell jokes and riddles")
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
            Jarvis.say("searching......")
            Jarvis.runAndWait()
            ans = ans.replace("go to ","")
            xyz = ("Enter some thing like ('.com','.io','.in'etc):")
            Jarvis.say(xyz)
            Jarvis.runAndWait()
            some = input("Enter some thing like ('.com','.io','.in'etc):")
            key = (f"https://www.{ans}{some}")
            webbrowser.open(key)
            Jarvis.say("Acording to the chrome this is what i found !!")
            Jarvis.runAndWait()
            input("Press enter to continue :")
        elif 'play' in ans and 'song' in ans:
            Jarvis.say("searching......")
            Jarvis.runAndWait()
            ans = ans.replace("play","")
            ans = ans.replace("song","")
            key = (f"https://www.youtube.com/results?search_query={ans}+song")
            webbrowser.open(key)
            Jarvis.say("Acording to the youtube this is what i found !!")
            Jarvis.runAndWait()
            input("Press enter to continue :")
        elif 'search' in ans:
            Jarvis.say("searching......")
            Jarvis.runAndWait()
            ans = ans.replace("search","")
            key = (f"https://www.google.com/search?q={ans}")
            webbrowser.open(key)
            Jarvis.say("Acording to the net this is what i found !!")
            Jarvis.runAndWait()
            input("Press enter to continue :")
        elif 'change voice' in ans :
            Command.Change_voice()
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
        elif 'open' in ans:
            Command.Open()
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
        elif 'history' in ans:
            print(history)
        elif 'riddle' in ans:
            io = 1
            jokes = random.choice(riddles)
            Jarvis.say(jokes)
            Jarvis.runAndWait()
        elif 'ppt' in ans :
            ppt = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(ppt)
        elif 'python' in ans:
            Jarvis.say("Which python code do you want to open ?")
            Jarvis.runAndWait()
            py = int(input("1 IDLE 3.7 - 32 bit\n2 3.7 - 32 bit\n3 Doc's 3.7 - 32 bit\n4 IDLE 3.6 - 32 bit\n5 3.6 - 32 bit\n6 Doc's 3.6 - 32 bit\n<^-^> "))
            if py == 1:              
                py1 = "C:\\Users\\rushil\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe"
                os.startfile(py1)
            elif py == 2:
                py2 = "C:\\Users\\rushil\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe"
                os.startfile(py2)
            elif py == 3:
                py3 = "C:\\Users\\rushil\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe -m pydoc -b"
                os.startfile(py3)
            elif py == 4:
                py4 = "C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\python.exe" 
                os.startfile(py4)
            elif py == 5:
                py5 = "C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\python.exe" 
                os.startfile(py5)
        elif 'open chrome' in ans:
            chrome = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrome)
        elif 'image.open<' in ans and '>' in ans :
            ans=ans.replace('image.open<','')   
            ans=ans.replace('>','')
            Jarvis.say("OK this might take a few moments")
            Jarvis.runAndWait()
            try :
                root = Tk()
                image_name = PhotoImage(file=ans)
                Button(root,image=image_name).pack()
                root.mainloop()
            except Exception as e :
                Jarvis.say(e)
                Jarvis.runAndWait()
        else:   
            Jarvis.say("invalid command")
            Jarvis.runAndWait()
            print("Sorry i can not do that")
            Jarvis.say("Should i search this on the net ?")
            Jarvis.runAndWait()
            y_n = input("{y/n} : ")
            if y_n == "y":
                key = (f"https://www.google.com/search?q={ans}")
                webbrowser.open(key)
                Jarvis.say(" Ok.. Acording to the net this is what i found !!")
                Jarvis.runAndWait()
            else:
                h=1
