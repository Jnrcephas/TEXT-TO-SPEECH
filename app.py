import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices') 

def speaknow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    
    setvoice(text, gender, speed)
    
def setvoice(text, gender, speed):
    if (gender == 'Male'):
        engine.setProperty('voice', voices[0].id)
        engine.say(text)
        engine.runAndWait()
    else:
        engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()

    if (speed == 'Fast'):
        engine.setProperty('rate', 250)
    elif (speed == 'Normal'):
        engine.setProperty('rate', 150)
    else:
        engine.setProperty('rate', 60)



def download():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    
    setvoice(text, gender, speed)
    
    file_path = filedialog.asksaveasfilename(defaultextension=".mp3")
    if file_path:
        engine.save_to_file(text, file_path)
        engine.runAndWait()




root= Tk()
root.title('Text To Speech App')
root.geometry('900x450+200+200')
root.resizable(False,False)
root.configure(bg='light blue')

image_icon=PhotoImage(file='speak.png')
root.iconphoto(False,image_icon)


Top_frame= Frame(root,bg="white",width=900,height=100)
Top_frame.place(x=0,y=0)
Logo=PhotoImage(file='logoo.png')
Label(Top_frame,image=Logo,bg='white').place(x=0,y=-20)
Label(Top_frame,text="CEPHAS' TEXT TO SPEECH",font='arial 20 bold',bg='white',fg='light blue').place(x=120,y=30)


########
text_area=Text(root,font='Roboto 20',bg='white',relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=150,width=500,height=250)

Label(root,text='VOICE',font='arial 15 bold',bg='light blue',fg='white').place(x=580,y=160)
Label(root,text='SPEED',font='arial 15 bold',bg='light blue',fg='white').place(x=760,y=160)


gender_combobox=Combobox(root,values=['Male','Female'],font='arial 14',state='r',width=10)
gender_combobox.place(x=550,y=200)
gender_combobox.set('Male')


speed_combobox=Combobox(root,values=['Fast','Normal','Slow'],font='arial 14',state='r',width=10)
speed_combobox.place(x=730,y=200)
speed_combobox.set('Normal')


imageicon=PhotoImage(file='speak.png')
btn=Button(root,text='Speak',compound=LEFT,image=imageicon,width=130,bg='yellow',font='arial 14 bold',command=speaknow)
btn.place(x=550,y=280)

imageicon2=PhotoImage(file='save.png')
save=Button(root,text='Save',compound=LEFT,image=imageicon2,bg='green',width=130,font='arial 14 bold',command=download)
save.place(x=730,y=280)


root.mainloop()
