#importing packages 
from tkinter import * 
import tkinter.messagebox

# Creating the initial window
window = Tk()
# Giving a title
window.title(" Python To-Do List ")
window.configure(bg="white")
window.geometry("600x450")

# Get the screen width and height to center the window
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set the window size and position it in the center of the screen
window_width = 600
window_height = 450
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Frame widget to hold the listbox and the scrollbar
frame_task = Frame(window)
frame_task.pack()

#add fuction 
def entertask():
    # A new window to pop up to take input
    input_text = ""

    def add():
        
        input_text = entry_task.get(1.0, "end-1c")
        if input_text == "":
            tkinter.messagebox.showwarning(title="Warning!", message="Please Enter some Text")
        else:
            listbox_task.insert(END, input_text)
            # Close the root1 window
            root1.destroy()

    root1 = Tk()
    root1.configure(bg="gray")
    root1.title("Add task")
    entry_task = Text(root1, width=40, height=5)
    entry_task.pack()
    button_temp = Button(root1, text="Add task", command=add,bg="white")
    button_temp.place(x=165,y=90)
   # Get the screen width and height to center the window
    screen_width = root1.winfo_screenwidth()
    screen_height = root1.winfo_screenheight()

    # Set the window size and position it in the center of the screen
    root1_width = 390
    root1_height = 150
    x = (screen_width - root1_width) // 2
    y = (screen_height - root1_height) // 2
    root1.geometry(f"{root1_width}x{root1_height}+{x}+{y}") 
    root1.mainloop()

#delet function
def deletetask():
    
    # Selects the selected item and then deletes it 
    selected = listbox_task.curselection()
    if not selected:
        tkinter.messagebox.showwarning(title="Warning!", message="Please select a task to delete.")
        return
    listbox_task.delete(selected[0])

#complet function
def markcompleted():
    marked = listbox_task.curselection()
    if not marked:
        tkinter.messagebox.showwarning(title="Warning!", message="Please select a task to mark as completed..")
        return
    temp = marked[0]
    # Store the text of selected item in a string
    temp_marked = listbox_task.get(marked)
    # Update it 
    temp_marked = temp_marked + " ✔"
    # Delete it then insert it 
    listbox_task.delete(temp)
    listbox_task.insert(temp, temp_marked)

#update function
def updatetask():
    selected = listbox_task.curselection()
    if not selected:
        tkinter.messagebox.showwarning(title="Warning!", message="Please select a task to update.")
        return

    def update():
        input_text = entry_task.get(1.0, "end-1c")
        if input_text == "":
            tkinter.messagebox.showwarning(title="Warning!", message="Please Enter some Text")
        else:
            listbox_task.delete(selected[0])
            listbox_task.insert(selected[0], input_text)
            # Close the root2 window
            root2.destroy()

    root2 = Tk()
    root2.configure(bg="gray")
    root2.title("Update task")
    entry_task = Text(root2, width=40, height=4)
    entry_task.insert(INSERT, listbox_task.get(selected[0]))
    entry_task.pack()
    button_temp = Button(root2, text="Update task", command=update,bg="white")
    button_temp.place(x=165,y=80)
    # Get the screen width and height to center the window
    screen_width = root2.winfo_screenwidth()
    screen_height = root2.winfo_screenheight()

    # Set the window size and position it in the center of the screen
    root2_width = 390
    root2_height = 150
    x = (screen_width - root2_width) // 2
    y = (screen_height - root2_height) // 2
    root2.geometry(f"{root2_width}x{root2_height}+{x}+{y}") 
    root2.mainloop()

# To hold items in a listbox
listbox_task = Listbox(frame_task, bg="light grey", fg="black", height=15, width=50, font="Helvetica")
listbox_task.pack(side=tkinter.LEFT)

# Scrollbar
scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT, fill=tkinter.Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

# Buttons
entry_button = Button(window, text="Add task", width=30, command=entertask)
entry_button.place(x=40,y=370)

update_button = Button(window, text="Update selected task", width=30, command=updatetask)
update_button.place(x=40,y=400)

delete_button = Button(window, text="Delete selected task", width=30, command=deletetask)
delete_button.place(x=310,y=370)

mark_button = Button(window, text="Mark as completed", width=30, command=markcompleted)
mark_button.place(x=310,y=400)

#main window
window.mainloop()
