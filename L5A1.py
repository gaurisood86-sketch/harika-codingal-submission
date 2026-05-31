from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("First window")
root.geometry("200x200")

def msg():
    messagebox.showwarning("ALERT!" ,"VIRUS FOUND IN YOUR SYSTEM")

button=Button(root , text="SCAN FOR VIRUS" , command=msg)
button.grid(row=2,column=2,padx=80,pady=80)

root.mainloop()