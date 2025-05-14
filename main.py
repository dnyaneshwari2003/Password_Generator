import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        character_list = ""

        if digits_var.get():
            character_list += string.digits  # 0-9
        if letters_var.get():
            character_list += string.ascii_letters  # A-Z and a-z
        if special_var.get():
            character_list += string.punctuation  # Special characters

        if not character_list:
            messagebox.showwarning("Warning", "Please select at least one character set.")
            return

        password = "".join(random.choice(character_list) for _ in range(length))
        password_var.set(password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for password length.")

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Password length input
tk.Label(root, text="Enter password length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Checkbuttons for character sets
digits_var = tk.BooleanVar()
letters_var = tk.BooleanVar()
special_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Digits (0-9)", variable=digits_var).pack()
tk.Checkbutton(root, text="Include Letters (a-z, A-Z)", variable=letters_var).pack()
tk.Checkbutton(root, text="Include Special Characters (!@#...)", variable=special_var).pack()

# Generate button
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

# Output
password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, width=30, font=("Courier", 12)).pack(pady=10)

# Run the GUI event loop
root.mainloop()
