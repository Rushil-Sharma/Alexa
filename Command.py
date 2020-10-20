def Quit():
    Jarvis.say("For saftey we will clear the screen")
    Jarvis.runAndWait()
    os.system('clear')
    sys.exit(0)
def Go_To():
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
def Play_Song():
    Jarvis.say("searching......")
    Jarvis.runAndWait()
    ans = ans.replace("play","")
    ans = ans.replace("song","")
    key = (f"https://www.youtube.com/results?search_query={ans}+song")
    webbrowser.open(key)
    Jarvis.say("Acording to the net this is what i found !!")
    Jarvis.runAndWait()
    input("Press enter to continue :")
def Search():
    Jarvis.say("searching......")
    Jarvis.runAndWait()
    ans = ans.replace("search","")
    key = (f"https://www.google.com/search?q={ans}")
    webbrowser.open(key)
    Jarvis.say("Acording to the net this is what i found !!")
    Jarvis.runAndWait()
    input("Press enter to continue :")
def Change_voice():
    voices = Jarvis.getProperty('voices')
    if x%2 == 0:
        Jarvis.setProperty('voice', voices[1].id)
    elif x%2 != 0:
        Jarvis.setProperty('voice', voices[0].id)
    x=x+1  
def Open():
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
        print("i am amazed can you do that for me :}")
    else:
        Jarvis.say("I have no answer to that question ")
        Jarvis.runAndWait()
        print("I have no answer to that question")
    d=d+1
def Image_Open():
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
def Invalid():
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