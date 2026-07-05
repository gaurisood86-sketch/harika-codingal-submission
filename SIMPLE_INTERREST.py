
import tkinter as tk

root = tk.Tk()
root.title("interest Calculator App")
root.geometry("400x400")

def calculate():
    p = float(entry_p.get())
    t = float(entry_t.get())
    r = float(entry_r.get())
    
    si = (p * t * r) / 100
    ci = p * (pow((1 + r / 100), t)) - p
    
    label_si_val.config(text=f"{si:.2f}")
    label_ci_val.config(text=f"{ci:.2f}")

tk.Label(root, text="Principle:").grid(row=0, column=0, padx=10, pady=10)
entry_p = tk.Entry(root)
entry_p.grid(row=0, column=1)

tk.Label(root, text="Time (years):").grid(row=1, column=0, padx=10, pady=10)
entry_t = tk.Entry(root)
entry_t.grid(row=1, column=1)

tk.Label(root, text="Rate of Interest (%):").grid(row=2, column=0, padx=10, pady=10)
entry_r = tk.Entry(root)
entry_r.grid(row=2, column=1)

btn = tk.Button(root, text="Calculate", command=calculate)
btn.grid(row=3, column=0, columnspan=2, pady=20)

tk.Label(root, text="Simple Interest:").grid(row=4, column=0, padx=10, pady=5)
label_si_val = tk.Label(root, text="0.00")
label_si_val.grid(row=4, column=1)

tk.Label(root, text="Compound Interest:").grid(row=5, column=0, padx=10, pady=5)
label_ci_val = tk.Label(root, text="0.00")
label_ci_val.grid(row=5, column=1)

root.mainloop()

