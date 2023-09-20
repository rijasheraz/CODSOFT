#importing packages 
from tkinter import * 
import tkinter.messagebox

# Creating window
window = Tk()
# Giving a title
window.title(" CALCULATOR ")
 
#resize image
window.resizable(0,0)
#geomerty of window
window.geometry("312x324")
#set screen width and height to center window
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

#window size and position it in the center of the screen
window_width=314
window_height=324
x=(screen_width-window_width)//2
y=(screen_height-window_height)//2
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

#click button condition to perform all numbers and operation
def click_button(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

#clear button condition to clear all text box
def clear_button():
    global expression
    expression = ""
    input_text.set("")

#equal button condition to perform add,sub,division,multiplication
def equal_button():
 global expression
 result = str(eval(expression))
 input_text.set(result)
 expression = ""
expression = ""
input_text = StringVar()


input_frame = Frame(window, width = 312, height = 50, bd = 0,
highlightbackground = "black", highlightcolor = "black", highlightthickness =1)
input_frame.pack(side = TOP)

input_field = Entry(input_frame, font = ('Times New Roman', 18, 'bold'), textvariable =
input_text, width = 50, bg = "#eee", bd = 0, justify = RIGHT)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10)


buttons_frame = Frame(window, width = 312, height = 272.5, bg = "black")
buttons_frame.pack()

clear = Button(buttons_frame, text = "Clear", fg = "black", width = 32, height =3, bd = 0, bg = "#eee",   command = lambda:clear_button(), font=("Times New Roman",10) ).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
divide = Button(buttons_frame, text = "/", fg = "black", width = 10, height = 3,bd = 0, bg = "#eee", command = lambda:click_button("/")).grid(row = 0, column = 3, padx = 1, pady = 1)

seven = Button(buttons_frame, text = "7", fg = "black", width = 10, height = 3,bd = 0, bg = "#fff",  command = lambda:click_button(7),font=("Times New Roman",10)).grid(row = 1, column = 0, padx = 1, pady = 1)
eight = Button(buttons_frame, text = "8", fg = "black", width = 10, height = 3,bd = 0, bg = "#fff",  command = lambda:click_button(8),font=("Times New Roman",10)).grid(row = 1, column = 1, padx = 1, pady = 1)
nine = Button(buttons_frame, text = "9", fg = "black", width = 10, height = 3,bd = 0, bg = "#fff", command = lambda:click_button(9),font=("Times New Roman",10)).grid(row = 1, column = 2, padx = 1, pady = 1)
multiply = Button(buttons_frame, text = "*", fg = "black", width = 10, height =3, bd = 0, bg = "#eee", command = lambda:click_button("*")).grid(row = 1, column = 3, padx = 1, pady = 1)

four = Button(buttons_frame, text = "4", fg = "black", width = 10, height = 3,bd = 0, bg = "#fff", command = lambda:click_button(4),font=("Times New Roman",10)).grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(buttons_frame, text = "5", fg = "black", width = 10, height = 3,bd = 0, bg = "#fff",  command = lambda:click_button(5),font=("Times New Roman",10)).grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(buttons_frame, text = "6", fg = "black", width = 10, height = 3, bd= 0, bg = "#fff", command = lambda: click_button(6),font=("Times New Roman",10)).grid(row= 2, column = 2, padx = 1, pady = 1)
minus = Button(buttons_frame, text = "-", fg = "black", width = 10, height = 3,bd = 0, bg = "#eee", command = lambda: click_button("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
one = Button(buttons_frame, text = "1", fg = "black", width = 10, height = 3, bd= 0, bg = "#fff",  command = lambda: click_button(1),font=("Times New Roman",10)).grid(row= 3, column = 0, padx = 1, pady = 1)
two = Button(buttons_frame, text = "2", fg = "black", width = 10, height = 3, bd= 0, bg = "#fff",  command = lambda: click_button(2),font=("Times New Roman",10)).grid(row= 3, column = 1, padx = 1, pady = 1)
three = Button(buttons_frame, text = "3", fg = "black", width = 10, height = 3,bd = 0, bg = "#fff", command = lambda:click_button(3),font=("Times New Roman",10)).grid(row = 3, column = 2, padx = 1, pady = 1)
plus = Button(buttons_frame, text = "+", fg = "black", width = 10, height = 3,bd = 0, bg = "#eee", command = lambda:click_button("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
# 4h. Fifth row includes 3 buttons, „0‟, „Decimal (.)‟, and „Equal To (=)‟:
zero = Button(buttons_frame, text = "0", fg = "black", width = 21, height = 3,bd = 0, bg = "#fff", command = lambda:click_button(0),font=("Times New Roman",10)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
point = Button(buttons_frame, text = ".", fg = "black", width = 10, height = 3,bd = 0, bg = "#eee", command = lambda:click_button(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
equals = Button(buttons_frame, text = "=", fg = "black", width = 10, height = 3,bd = 0, bg = "#eee", command = lambda:equal_button()).grid(row = 4, column = 3, padx = 1, pady = 1)

#calling main window 
window.mainloop()
