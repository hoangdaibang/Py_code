from email.mime import image
from msilib.schema import Font
from tkinter import font
from tkinter.font import BOLD
from turtle import width
from django.shortcuts import render
import googletrans 
from tkinter import *
from PIL import Image,ImageTk
from googletrans import Translator


root=Tk()
root.title('Google translator')
root.geometry("500x630")
root.iconbitmap('logo.ico')

load=Image.open('background.png')
render=ImageTk.PhotoImage(load)
img=Label(root,image=render)
img.place(x=0,y=0)

name=Label(root,text="Translator",fg="#FFFFFF",bd=0,bg="#03152D")
name.config(font=("Arial",30))
name.pack(pady=10)

box=Text(root,width=28,height=8,font=("ROBOTO",16))
box.pack(pady=10)

button_frame=Frame(root).pack(side=BOTTOM)

def clear():
    box.delete(1.0,END)
    box1.delete(1.0,END)
def translate():
    INPUT=box.get(1.0,END)
    print(INPUT)
    t=Translator()
    a=t.translate(INPUT,src="vi",dest="en")
    b=a.text
    print(b)
    box1.insert(END,b)

clear_button=Button(button_frame,text="Clear text",font=("Arial",10,"bold"),fg='#FFFFFF',bg="#303030",command=clear)
clear_button.place(x=150,y=310)
translate_button=Button(button_frame,text="Translate text",font=("Arial",10,"bold"),fg='#FFFFFF',bg="#303030",command=translate)
translate_button.place(x=290,y=310)
box1=Text(root,width=28,height=8,font=("ROBOTO",16))
box1.pack(pady=50)

root.mainloop()