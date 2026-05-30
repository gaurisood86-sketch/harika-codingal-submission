from tkinter import *
root=Tk()
root.title("form sumbmission")
root.geometry("200x300")
root.configure(bg="lavender")

def data():
    print("Data was sumbitted.")

label=Label(root , text="Welcome to tkinter" , font=("arial", 12))
entry=Entry(root , width=20)
button=Button(root , text="sumbit" , command=data)

label.grid(row=0,column=0,columnspan=2,pady=5)
entry.grid(row=1,column=0,padx=5,pady=5)
button.grid(row=2,column=1,padx=5,pady=5)

root.mainloop()