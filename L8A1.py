from tkinter import *

root=Tk()
root.title("NUMBER PAD")
root.geometry("500x300")

nums=[[9,8,7],[6,5,4],[3,2,1],['#',0,'*']]

for i in range(4):
    root.columnconfigure(i,weight=1,minsize=75)
    root.rowconfigure(i,weight=1,minsize=50)
for i in range(4):
    for j in range(3):
        frame=Frame(
            master=root,
            relief=SUNKEN,
            borderwidth=1,
            bg='lightblue'
        
        )
        frame.grid(row=i,column=j)
        label=Label(master=frame,text=nums[i][j],bg='black')
        label.pack(padx=3,pady=3)

root.mainloop()


    