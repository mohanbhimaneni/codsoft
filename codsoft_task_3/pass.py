import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password(length, include_lowercase, include_uppercase, include_numbers, include_special_chars):
    characters = ''
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    # To Ensure at least one character from each selected category
    password = ''
    password += random.choice(string.ascii_lowercase) if include_lowercase else ''  # For adding lower, (only if selected)
    password += random.choice(string.ascii_uppercase) if include_uppercase else ''  # For adding upper, (only if selected)
    password += random.choice(string.digits) if include_numbers else ''  # For adding digit, (only if selected)
    password += random.choice(string.punctuation) if include_special_chars else ''  # For adding special char, (only if selected)

    # radomly add others
    password += ''.join(random.choice(characters) for _ in range(length - len(password)))

    # Shuffle the password for randomness
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

def generate_password_gui():
    def on_generate_button_click():
        try:
            password_length = int(length_entry.get())
        except ValueError:
            result_label.config(text="Invalid input. Please enter a valid number.")
            return

        include_lowercase = lowercase_var.get()
        include_uppercase = uppercase_var.get()
        include_numbers = numbers_var.get()
        include_special_chars = special_chars_var.get()

        password = generate_password(password_length, include_lowercase, include_uppercase, include_numbers, include_special_chars)
        result_label.config(text=f"Generated Password: {password}")

    # Create the main window
    window = tk.Tk()
    window.title("Password Generator")
    window.geometry("350x350")

    # Password Length Entry
    length_label = tk.Label(window, text="Enter Password Length:")
    length_label.pack(pady=5)
    length_entry = tk.Entry(window)
    length_entry.pack(pady=5)

    #  Checkboxes Complexity selection
    complexity_label = tk.Label(window, text="Select Complexity:")
    complexity_label.pack(pady=5)
    lowercase_var = tk.BooleanVar()
    lowercase_checkbox = tk.Checkbutton(window, text="Lowercase", variable=lowercase_var)
    lowercase_checkbox.pack()
    uppercase_var = tk.BooleanVar()
    uppercase_checkbox = tk.Checkbutton(window, text="Uppercase", variable=uppercase_var)
    uppercase_checkbox.pack()
    numbers_var = tk.BooleanVar()
    numbers_checkbox = tk.Checkbutton(window, text="Numbers", variable=numbers_var)
    numbers_checkbox.pack()
    special_chars_var = tk.BooleanVar()
    special_chars_checkbox = tk.Checkbutton(window, text="Special Characters", variable=special_chars_var)
    special_chars_checkbox.pack()

    # Generate Button
    generate_button = tk.Button(window, text="Generate Password", command=on_generate_button_click)
    generate_button.pack(pady=10)

    # Result Label
    result_label = tk.Label(window, text="")
    result_label.pack(pady=10)

   
    window.mainloop()


generate_password_gui()
