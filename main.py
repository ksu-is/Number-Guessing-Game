import tkinter as tk
import random

secret_number = 0
attempts = 0

def start_game():
    global secret_number, attempts
    attempts = 0
    difficulty = difficulty_var.get()
    
    if difficulty == "Easy":
        max_val = 50
    elif difficulty == "Medium":
        max_val = 100
    else:
        max_val = 200

    secret_number = random.randint(1, max_val)
    instruction_label.config(text=f"Guess a number between 1 and {max_val}:")
    result_label.config(text="")
    entry.delete(0, tk.END)
    submit_button.config(state="normal")

def check_guess():
    global attempts
    try:
        guess = int(entry.get())
        attempts += 1
        if guess < secret_number:
            result_label.config(text="Too low!")
        elif guess > secret_number:
            result_label.config(text="Too high!")
        else:
            result_label.config(text=f"You got it in {attempts} tries!")
            submit_button.config(state="disabled")
    except ValueError:
        result_label.config(text="Please enter a number!")

root = tk.Tk()
root.title("Number Guessing Game with Difficulty")
root.geometry("350x250")

difficulty_var = tk.StringVar(value="Medium")

tk.Label(root, text="Select Difficulty:").pack()
tk.Radiobutton(root, text="Easy (1-50)", variable=difficulty_var, value="Easy").pack()
tk.Radiobutton(root, text="Medium (1-100)", variable=difficulty_var, value="Medium").pack()
tk.Radiobutton(root, text="Hard (1-200)", variable=difficulty_var, value="Hard").pack()

start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack(pady=10)

instruction_label = tk.Label(root, text="Guess a number:")
instruction_label.pack(pady=5)

entry = tk.Entry(root)
entry.pack()

submit_button = tk.Button(root, text="Submit Guess", command=check_guess)
submit_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
  
