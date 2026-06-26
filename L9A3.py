from tkinter import *
import random

root=Tk()
root.title('ROCK,PAPER,SCISSORS')
root.geometry('400x400')
root.configure('blue')

choices=['rock','paper','scissors']

user_label=Label(root,text='YOUR CHOICE',font='arial')
user_label.pack(pady=10)

result_label=Label(root,text='',font='arial',fg='pink')
result_label.pack(pady=20)

comp_label=Label(root,text='',font='arial')
comp_label.pack(pady=30)

def play(user_choice):
    comp_choice=random.choice(choices)
    comp_label.config(text=f'computer choice:{comp_choice}')

    if user_choice==comp_choice:
        result="IT'S A TIE!"
    elif(user_choice=='rock' and comp_choice=='scissors')

