import tkinter as Tk
import random

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("450x400")
root.configure(bg="#2C3E50")

CHOICES = ["Rock", "Paper", "Scissors"]

def play_round(user_choice):
    program_choice = random.choice(CHOICES)
    
    
    user_display.config(text=user_choice)
    program_display.config(text=program_choice)
    
    
    if user_choice == program_choice:
        result_text = "It's a Tie! 🤝"
        result_color = "#F1C40F"
    elif (user_choice == "Rock" and program_choice == "Scissors") or \
         (user_choice == "Paper" and program_choice == "Rock") or \
         (user_choice == "Scissors" and program_choice == "Paper"):
        result_text = "You Win! 🎉"
        result_color = "#2ECC71"
    else:
        result_text = "Program Wins! 🤖"
        result_color = "#E74C3C"
         

    winner_label.config(text=result_text, fg=result_color)

def reset_game():
    user_display.config(text="-")
    program_display.config(text="-")
    winner_label.config(text="Make Your Move!", fg="#ECF0F1")


title_label = tk.Label(root, text="Rock Paper Scissors", font=("Helvetica", 18, "bold"), bg="#2C3E50", fg="#ECF0F1")
title_label.pack(pady=15)

display_frame = tk.Frame(root, bg="#2C3E50")
display_frame.pack(pady=20)

user_frame = tk.Frame(display_frame, bg="#34495E", padx=15, pady=10)
user_frame.grid(row=0, column=0, padx=20)
tk.Label(user_frame, text="YOUR MOVE", font=("Helvetica", 10, "bold"), bg="#34495E", fg="#BDC3C7").pack()
user_display = tk.Label(user_frame, text="-", font=("Helvetica", 16, "bold"), bg="#34495E", fg="#1ABC9C")
user_display.pack(pady=5)

vs_label = tk.Label(display_frame, text="VS", font=("Helvetica", 14, "bold"), bg="#2C3E50", fg="#ECF0F1")
vs_label.grid(row=0, column=1)

program_frame = tk.Frame(display_frame, bg="#34495E", padx=15, pady=10)
program_frame.grid(row=0, column=2, padx=20)
tk.Label(program_frame, text="PROGRAM", font=("Helvetica", 10, "bold"), bg="#34495E", fg="#BDC3C7").pack()
program_display = tk.Label(program_frame, text="-", font=("Helvetica", 16, "bold"), bg="#34495E", fg="#E67E22")
program_display.pack(pady=5)

winner_label = tk.Label(root, text="Make Your Move!", font=("Helvetica", 16, "bold"), bg="#2C3E50", fg="#ECF0F1")
winner_label.pack(pady=15)

button_frame = tk.Frame(root, bg="#2C3E50")
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="🪨 Rock", font=("Helvetica", 11, "bold"), width=8, bg="#95A5A6", command=lambda: play_round("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="📄 Paper", font=("Helvetica", 11, "bold"), width=8, bg="#95A5A6", command=lambda: play_round("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(button_frame, text="✂️ Scissors", font=("Helvetica", 11, "bold"), width=8, bg="#95A5A6", command=lambda: play_round("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

reset_btn = tk.Button(root, text="🔄 Reset Game", font=("Helvetica", 10, "bold"), bg="#3498DB", fg="white", width=12, command=reset_game)
reset_btn.pack(pady=20)

root.mainloop()
