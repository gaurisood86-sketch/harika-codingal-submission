from tkinter import *

root=Tk()
root.title('LOGIN APP')
root.geometry('500x400')

frame=Frame(master=root,width=200,height=300,bg='black')

label1=Label(frame,text='FULL NAME',bg='white',fg='blue',width=12)
label2=Label(frame,text="EMAIL ID",bg='white',fg='blue',width=12)
label3=Label(frame,text="ENTER PASSWORD",bg='white',fg='blue',width=12)

name_entry=Entry(frame)
email_entry=Entry(frame)
password_entry=Entry(frame,show='*')

