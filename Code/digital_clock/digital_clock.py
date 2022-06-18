from cProfile import label
from tkinter import *
from tkinter.ttk import *
from time import strftime

def clock():
    String=strftime('%I:%M:%S:%p')
    label.config(text=String)
    label.after(1000,clock)
    

root=Tk()
root.title("Digital Clock")
label=Label(root,font=("digital-7",100),background='white',foreground='red')
label.pack(anchor='center')
clock()

root.mainloop()