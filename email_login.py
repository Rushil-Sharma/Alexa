from tkinter import *
import pyttsx3 as pyt
import jarvis
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
    if '.' in x:
        r=r+1
    else:
        Jarvis.say("I think you missed the 'dot' ")
        Jarvis.runAndWait()
    if '@' in x:
        r=r+1
    else:
        Jarvis.say("I think you missed the at the rate symbol ")
        Jarvis.runAndWait()
    if 'gmail' in x:
        r=r+1
    else:
        Jarvis.say("Put a gmail or yahoo")
        Jarvis.runAndWait()
    if 'com' in x:
        r = r + 1
    else:
        Jarvis.say("I think you missed the .com ")
        Jarvis.runAndWait()
    if r == 4:
        Jarvis.say("You are verified now close this screen for safety")
        Jarvis.runAndWait()
        root.mainloop()
        jarvis.main_code()
Submit = Button(root,text='Submit',font=('Helvatica',30),fg='grey',bg='gold',command=verification)
Submit.grid(row=3,column=1,columnspan=2)
Jarvis.say("Ok . . . now you can enter your email")
Jarvis.runAndWait()
root.mainloop()