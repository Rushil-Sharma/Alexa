import pyttsx3 as pyt
import os
import sys 
import time 
import webbrowser
import wikipedia

Jarvis = pyt.init()
Jarvis.say("Hello There")
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
x=d=0
while True:
    ask_q = (name,"What may i help you with : ")
    Jarvis.say(ask_q)
    Jarvis.runAndWait()
    ans = input("Enter A Command \n<^-^> ")
    if 'quit' in ans:
        Jarvis.say("Ok bye")
        Jarvis.runAndWait()
        sys.exit(0)
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
        Jarvis.say("Acording to the microsoft edge this is what i found !!")
        Jarvis.runAndWait()
        input("Press enter to continue :")
    elif 'play' in ans and 'song' in ans:
        Jarvis.say("searching......")
        Jarvis.runAndWait()
        ans = ans.replace("play","")
        ans = ans.replace("song","")
        key = (f"https://www.youtube.com/results?search_query={ans}+song")
        webbrowser.open(key)
        Jarvis.say("Acording to the net this is what i found !!")
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
        voices = Jarvis.getProperty('voices')
        if x%2 == 0:
            Jarvis.setProperty('voice', voices[1].id)
        elif x%2 != 0:
            Jarvis.setProperty('voice', voices[0].id)
        x=x+1  
    elif 'time' in ans:
        time_now = time.strftime("%H:%M:%S")
        Jarvis.say(time_now)
        Jarvis.runAndWait()
    elif 'your name' in ans:
        Jarvis.say("I am jarvis your persional assistent")
        Jarvis.runAndWait()
    elif 'open youtube' in ans :
        webbrowser.open("youtube.com")
    elif 'open google' in ans :
        webbrowser.open("google.com")
    elif 'open ppt' in ans:
        ppt = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
        os.startfile(ppt)
    elif 'open chrome' in ans:
        chrome = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(chrome)
    elif 'math' in ans:
        Jarvis.say("Ok Loading operators . . Compiling code . . Done !!! ")
        Jarvis.runAndWait()
        lolololol()
    elif 'krunker' in ans:
        Jarvis.say("Ok Loading game . . Compiling guns . . Done !!! ")
        Jarvis.runAndWait()
        Jarvis.say("Enter your username here")
        Jarvis.runAndWait()
        user = input("Enter : ")
        if 'sorry' in user :
            if '176' in user :
                if '[W1NK]' in user :
                    webbrowser.open("https://krunker.io")
                else:
                    print("Not correct")
            else:
                print("Not correct")
        else:
            print("Not correct")
    elif '?' in ans :
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
            print("i am amazed can you do that for me :}")
        else:
            Jarvis.say("I have no answer to that question ")
            Jarvis.runAndWait()
            print("I have no answer to that question")
        d=d+1
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
            sp = ("Ok also try out this : quit ,tell the time,what is your name,can you open youtube,open google,open ppt,open chrome,can you do some math,search (anything) \ krunker")
            print("Ok also try out this : quit\ntell the time\nwhat is your name\ncan you open youtube\nopen google\nopen ppt\nopen chrome\ncan you do some math\nsearch (anything)\nOr\nkrunker")
            Jarvis.say(sp)
            Jarvis.runAndWait()
# The End :)