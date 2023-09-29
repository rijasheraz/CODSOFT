import string
import random
import tkinter as tk
from tkinter import ttk

# Function to generate a random password
def generate_password():
    length = int(length_entry.get())
    select_characters = ""

    if include_digits.get():
        select_characters += string.digits
    if include_letters.get():
        select_characters += string.ascii_letters
    if include_special_chars.get():
        select_characters += string.punctuation

    if not select_characters:
        result_label.config(text="Please select at least one character set.")
        return

    password = [random.choice(select_characters) for _ in range(length)]
    password_str = "".join(password)
    result_label.config(text="Random Password: " + password_str)

# Create the main window
window = tk.Tk()
window.title(" Generate Password ")
length_label = ttk.Label(window, text="GENERATE PASSWORD ", font=("Times New Roman", 15,"bold"))
length_label.place(x=100, y=10)
#resize image
window.resizable(0,0)

#set screen width and height to center window
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

#window size and position it in the center of the screen
window_width=400
window_height=324
x=(screen_width-window_width)//2
y=(screen_height-window_height)//2
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create and place widgets
font_style = ("Helvetica", 12.5)

# Create a custom style for the checkboxes
style = ttk.Style()
style.configure("Custom.TCheckbutton", font=12)


# Create and pack widgets
length_label = ttk.Label(window, text="Enter password length:", font=("Helvetica", 13))
length_label.place(x=10, y=70)
length_entry = ttk.Entry(window)
length_entry.place(x=180, y=70)

include_digits = tk.BooleanVar()
include_letters = tk.BooleanVar()
include_special_chars = tk.BooleanVar()

digits_check = ttk.Checkbutton(window, text="Include Digits (0-9)", variable=include_digits, style="Custom.TCheckbutton")
letters_check = ttk.Checkbutton(window, text="Include Letters (a-zA-Z)", variable=include_letters, style="Custom.TCheckbutton")
special_chars_check = ttk.Checkbutton(window, text="Include Special Characters", variable=include_special_chars,style="Custom.TCheckbutton")

digits_check.place(x=10, y=99)
letters_check.place(x=10, y=125)
special_chars_check.place(x=10, y=150)

generate_button = ttk.Button(window, text="Generate Password", command=generate_password, style="Custom.TButton")
generate_button.place(x=109, y=200)

result_label = ttk.Label(window, text="", font=("Times New Roman", 14))
result_label.place(x=80, y=230)

# Start the GUI event loop
window.mainloop()

