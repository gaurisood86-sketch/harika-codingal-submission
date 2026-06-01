import string
import random
from tkinter import *
from tkinter import messagebox

def generate():
    try:
        length = int(entry_len.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive number for length.")
        return
    
    chars = ""
    if var_lower.get(): chars += string.ascii_lowercase
    if var_upper.get(): chars += string.ascii_uppercase
    if var_digit.get(): chars += string.digits
    if var_special.get(): chars += string.punctuation
    
    if not chars:
        messagebox.showwarning("Selection Error", "Please select at least one character type.")
        return
        
    pwd = "".join(random.choice(chars) for _ in range(length))
    messagebox.showinfo("Generated Password", f"Your new password is:\n\n{pwd}")

root = Tk()
root.title("Random Password Generator")
root.geometry("350x280")
root.resizable(False, False)

Label(root, text="Password Length:").pack(pady=5)
entry_len = Entry(root, width=10)
entry_len.pack()
entry_len.insert(0, "12")

var_lower = BooleanVar(value=True)
var_upper = BooleanVar(value=True)
var_digit = BooleanVar(value=True)
var_special = BooleanVar(value=True)

Checkbutton(root, text="Include Lowercase (a-z)", variable=var_lower).pack(anchor=W, padx=50)
Checkbutton(root, text="Include Uppercase (A-Z)", variable=var_upper).pack(anchor=W, padx=50)
Checkbutton(root, text="Include Digits (0-9)", variable=var_digit).pack(anchor=W, padx=50)
Checkbutton(root, text="Include Special Characters", variable=var_special).pack(anchor=W, padx=50)

Button(root, text="Generate Password", command=generate).pack(pady=15)

root.mainloop()
