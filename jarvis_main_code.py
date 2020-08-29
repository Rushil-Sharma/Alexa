import pyttsx3 as pyt
import os
import sys 
import time 
import webbrowser
import wikipedia
import random
import smtplib
o='10101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010'
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
for i in range(10):
    code = """import pyttsx3 as pyt
    import os
    import sys 
    import time 
    import webbrowser
    import wikipedia
    import random
    import smtplib
    o='10101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010'
    joke=[
        '1 ...... What do you call a dinosaur that is sleeping? , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,
        A dino-snore!',

        '2 ...... What is fast, loud and crunchy? , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,
        A rocket chip!',

        '3 ...... Why did the teddy bear say no to dessert? , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,
        Because she was stuffed.',

        '4 ...... What has ears but cannot hear? , ,  , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,
        A cornfield.',

        '5 ...... What did the left eye say to the right eye? , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,
        Between us, something smells!',

        '6 ...... What do you get when you cross a vampire and a snowman? , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,
        Frost bite!',

        '7 ...... What did one plate say to the other plate? , ,  , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,
        Dinner is on me!',

        '8 ...... Why did the student eat his homework? , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,
        Because the teacher told him it was a piece of cake!',

        '9 ...... When you look for something, why is it always in the last place you look? , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,
        Because when you find it, you stop looking.',

        '10 ...... What is brown, hairy and wears sunglasses? , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,
        A coconut on vacation.'
    ]
    riddles=[
        '1. Riddle: What has to be broken before you can use it?
        Answer: An egg',

        '2. Riddle: I’m tall when I’m young, and I’m short when I’m old. What am I?
        Answer: A candle,

        '3. Riddle: What month of the year has 28 days?
        Answer: All of them',

        '4. Riddle: What is full of holes but still holds water?
        Answer: A sponge',

        '5. Riddle: What question can you never answer yes to?
        Answer: Are you asleep yet?',

        '6. Riddle: What is always in front of you but can’t be seen?
        Answer: The future',

        '7. Riddle: There’s a one-story house in which everything is yellow. Yellow walls, yellow doors, yellow furniture. What color are the stairs?
        Answer: There aren’t any—it’s a one-story house.',

        '8. Riddle. What can you break, even if you never pick it up or touch it?
        Answer: A promise',

        'Riddle: What goes up but never comes down?
        Answer: Your age',

        ' Riddle: A man who was outside in the rain without an umbrella or hat didn’t get a single hair on his head wet. Why?
        Answer: He was bald.'
    ]
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
    Jarvis_name = 'Jarvis'
    x=d=0
    print("Enter A Command or type index<> for all the commands :")
    while True:
        if name == "no":
            ask_q = ("What may i help you with : ")
        else:
            ask_q = (name,"What may i help you with : ")
        Jarvis.say(ask_q)
        Jarvis.runAndWait()
        ans = input("<^-^> ")
        if 'quit' in ans:
            Jarvis.say("Ok bye")
            Jarvis.runAndWait()
            sys.exit(0)
        elif 'hi' in ans or 'hey' in ans or 'hello' in ans or 'sup' in ans:
            print("hello i am",Jarvis_name)
            Jarvis.say('Hello')
            Jarvis.runAndWait()
        elif 'index<>' in ans:
            print("type<type anything here>\nclear<> : to clear the screen\ngo to (any website)\nplay (some) song\nsearch (anything here)\nchange your voice\nriddle me !\ntell me a joke\nhey what is the time ?\nopen ppt app\nopen python\ncan you do some math\n\n\n\n")
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
            os.system('cls')
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
            key = (f"https://www.{ans }{ some}")
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
            J_n = ("I am",Jarvis_name,"You can also change my voice by the command : change your name and also change your name by the command : chsnge my name ")
            Jarvis.say(J_n)
            Jarvis.runAndWait()
        elif 'open youtube' in ans :
            webbrowser.open("youtube.com")
        elif 'open google' in ans :
            webbrowser.open("google.com")
        elif 'open' in ans:
            if 'ppt' in ans :
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
        elif 'math' in ans:
            Jarvis.say("Ok Loading operators . . Compiling code . . Done !!! ")
            Jarvis.runAndWait()
            lolololol()
        elif 'hack<>' in ans:
            Password = input("Please Enter Password : ")
            Jarvis.say("Succsesfully hacked !!! Screen . . . . playing fortninte . . . . . . . . . , trying to get bttle pass . . . . .. . . . . . . . . .  BUT utter fail")
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
        elif '*-'in ans and "-*" in ans :
            ans = ans.replace("*-","")
            ans = ans.replace("-*","")
            hi = ans.upper()
            print(hi)
        elif 'send email' in ans :
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=new")
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
                """
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
Jarvis_name = 'Jarvis'
x=d=0
print("Enter A Command or type index<> for all the commands :")
while True:
    if name == "no":
        ask_q = ("What may i help you with : ")
    else:
        ask_q = (name,"What may i help you with : ")
    Jarvis.say(ask_q)
    Jarvis.runAndWait()
    ans = input("<^-^> ")
    if 'quit' in ans:
        Jarvis.say("Ok bye")
        Jarvis.runAndWait()
        sys.exit(0)
    elif 'hi' in ans or 'hey' in ans or 'hello' in ans or 'sup' in ans:
        print("hello i am",Jarvis_name)
        Jarvis.say('Hello')
        Jarvis.runAndWait()
    elif 'index<>' in ans:
        print("type<type anything here>\nclear<> : to clear the screen\ngo to (any website)\nplay (some) song\nsearch (anything here)\nchange your voice\nriddle me !\ntell me a joke\nhey what is the time ?\nopen ppt app\nopen python\ncan you do some math\n\n\n\n")
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
        os.system('cls')
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
        J_n = ("I am",Jarvis_name,"You can also change my voice by the command : change your name and also change your name by the command : chsnge my name ")
        Jarvis.say(J_n)
        Jarvis.runAndWait()
    elif 'open youtube' in ans :
        webbrowser.open("youtube.com")
    elif 'open google' in ans :
        webbrowser.open("google.com")
    elif 'code' in ans:
        print(code)
        Jarvis.say('This is my misure code you want me to read it out ?')
        Jarvis.runAndWait()
        code_dictate = input("::  ")
        if code_dictate == 'yes' :
            Jarvis.say(code)
            Jarvis.runAndWait()
    elif 'open' in ans:
        if 'ppt' in ans :
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
    elif 'math' in ans:
        Jarvis.say("Ok Loading operators . . Compiling code . . Done !!! ")
        Jarvis.runAndWait()
        lolololol()
    elif 'hack<>' in ans:
        Password = input("Please Enter Password : ")
        Jarvis.say("Succsesfully hacked !!! Screen . . . . playing fortninte . . . . . . . . . , trying to get bttle pass . . . . .. . . . . . . . . .  BUT utter fail")
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
    elif '*-'in ans and "-*" in ans :
        ans = ans.replace("*-","")
        ans = ans.replace("-*","")
        hi = ans.upper()
        print(hi)
    elif 'send email' in ans :
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=new")
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
    elif 'open youtube' in ans :
        webbrowser.open("youtube.com")
    elif 'open google' in ans :
        webbrowser.open("google.com")
    elif 'open' in ans:
        if 'ppt' in ans :
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
    elif '*-'in ans and "-*" in ans :
        ans = ans.replace("*-","")
        ans = ans.replace("-*","")
        hi = ans.upper()
        print(hi)
    elif 'send email to mom' in ans :
        try :
            Jarvis.say("What should i say ? ")
            Jarvis.runAndWait()
            content = input("Enter : ")
            to = "barchepurva@gmail.com"
            send(to,content)
            Jarvis.say("Email sent")
            Jarvis.runAndWait()
        except Exception as e:
            print(e)
            Jarvis.say("""The term 'Send' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the 
            name, or if a path was included, verify that the path is correct and try again.
            At line:1 char:1
            + Send email
            + ~~
                + CategoryInfo          : ObjectNotFound: (ww:String) [], CommandNotFoundException
                + FullyQualifiedErrorId : CommandNotFoundException
            What i mean is it is an error my boyy""")
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
# The End :)
