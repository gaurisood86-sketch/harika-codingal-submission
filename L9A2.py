from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("VIRUS DETECTOR")
root.geometry('400x400')

def msg():
    messagebox.showwarning("ALERT","VIRUS DETECTED!")

button=Button(root,text='SCAN FOR VIRUS',command=msg)
button.place(x=40,y=70)

root.mainloop()