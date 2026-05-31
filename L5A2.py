from tkinter import *
from tkinter import messagebox
from PIL import Image , ImageTk 

root=Tk()
root.title("Window")
root.geometry("400x400")
 
def show_image():
    img_window=Toplevel(root)
    img_window.title("First Window")

    img=Image.open("yes-bank.jpg")
    # img=img.resize(200,200)
    img_Tk=ImageTk.PhotoImage(img)

    img_label=Label(img_window , image=img_Tk)
    img_label.image=img_Tk
    img_label.pack()

def show_message():
    messagebox.showinfo("HELLO","HI MY FRIEND")

def open_top_window():
    top=Toplevel(root)
    top.title("TOP WINDOW!")
    top.geometry("150x200")
    Label(top , text="NEW TOP WINDOW! " , font=("Arial" , 12)).pack(pady=20)

button1=Button(root , text="IMAGE" , command=show_image)
button1.pack(pady=20)

button2=Button(root , text="TEXT" , command=show_message)
button2.pack(pady=20)

button3=Button(root , text="TOP WINDOW" , command=open_top_window)
button3.pack(pady=20)

root.mainloop()
