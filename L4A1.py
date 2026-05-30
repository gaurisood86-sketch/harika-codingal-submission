from tkinter import *
root=Tk()
root.title("this is my first tkinter window")
root.geometry("300x400")
root.configure(bg="lightblue")
entry=Entry(root)
entry.place(x=10 , y=40)

root.mainloop()

