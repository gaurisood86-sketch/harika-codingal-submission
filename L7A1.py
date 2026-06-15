from tkinter import *
from datetime import date

root=Tk()
root.title("Getting started with widgets!")
root.geometry('300x300')

label_1=Label(text="hey there!",fg="white",bg="blue",height=1,width=300)

label_2=Label(text="FULL NAME:",bg="pink")
name_entry=Entry()

def display():
    name=name_entry.get()
    global message
    greet="HELLO!"+name+"\n"
    message="Hello welcome to the apllication!\nToday's date is:"

    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())

text_box=Text(height=3)
button=Button(text="HERE",command=display,fg="black",bg="lightblue")

label_1.pack()
label_2.pack()
name_entry.pack()
button.pack()
text_box.pack()

root.mainloop()







    