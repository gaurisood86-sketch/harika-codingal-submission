import tkinter as tk


def convert():
    try:
        inches = float(entry.get())
        cm = inches * 2.54
        result_label.config(text=f"{cm:.2f} cm")
    except ValueError:
        result_label.config(text="Invalid Input")

root = tk.Tk()
root.title('length converter app')
root.geometry('400x400')

tk.Label(root, text="Enter Inches:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

convert_btn = tk.Button(root, text="Convert", command=convert)
convert_btn.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

root.mainloop()
