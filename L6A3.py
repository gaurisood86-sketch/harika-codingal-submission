import tkinter as tk

def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2

        result_display.delete(1.0, tk.END)
        result_display.insert(tk.END, f"The product is: {product}")
    except ValueError:
        result_display.delete(1.0, tk.END)
        result_display.insert(tk.END, "Please enter valid numbers.")

root = tk.Tk()
root.geometry("400x300")

root.title("Getting Started with Widgets")

desc_label = tk.Label(root, text="This app calculates the product of two numbers.", fg="blue")
desc_label.pack(pady=5)

tk.Label(root, text="Enter first number:").pack()
entry1 = tk.Entry(root, bg="#e0f7fa")
entry1.pack(pady=2)

tk.Label(root, text="Enter second number:").pack()
entry2 = tk.Entry(root, bg="#e0f7fa")
entry2.pack(pady=2)

calc_button = tk.Button(root, text="Calculate Product", command=calculate_product, bg="#4caf50", fg="white")
calc_button.pack(pady=10)

result_display = tk.Text(root, height=2, width=30, bg="#fff9c4")
result_display.pack(pady=5)

root.mainloop()
