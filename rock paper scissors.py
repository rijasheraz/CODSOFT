import tkinter as tk
import random

# Function to the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Function to handle user's choice
def make_choice(choice):
    computer_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer_choices)
    result = determine_winner(choice, computer_choice)
    result_label.config(text=f"Computer chose {computer_choice}. {result}")

# Create the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")
 
label = tk.Label(window, text="welcome", bg="white",fg="black", font=("Times New Roman,", 15,"bold"))
label.place(x=230, y=1)

#now add background color
window.configure(bg="white")
#resize image
window.resizable(0,0)

# Get the screen width and height to center the window
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set the window size and position it in the center of the screen
window_width = 499
window_height = 400
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create a Canvas widget to display the image
# Load and display the image using PhotoImage ( your image file path)
image = tk.PhotoImage(file="D:\inter code\intern.png")  # Use the image file format
image= image.zoom(1)# add zoom command code
#image=image.subsample(1)# decrease resolution of image
image_label2 = tk.Label(window, image=image)
image_label2.place(x=150,y=40)
 
# Create buttons for rock, paper, and scissors  
rock_button = tk.Button(window, text="Rock", command=lambda: make_choice("  rock  "),bg="white", fg="black", font=("Times New Roman", 15), width=10, height=1) 
paper_button = tk.Button(window, text="Paper", command=lambda: make_choice(" paper "), bg="white",fg="black", font=("Times New Roman", 15), width=10, height=1)
scissors_button = tk.Button(window, text="Scissors", command=lambda: make_choice("scissors"), bg="white",fg="black", font=("Times New Roman", 15), width=10, height=1)

rock_button.place(x=90, y=290)
paper_button.place(x=210, y=290)
scissors_button.place(x=330, y=290)

# Create a label to display the result
result_label = tk.Label(window, text="", bg="white",fg="red", font=("Times New Roman", 14))
result_label.place(x=110, y=350)

# main window call
window.mainloop()
