import customtkinter as ctk
from CTkListbox import *

root = ctk.CTk()
root.geometry("750x750")
root.title("ToDo APP")

# Funcs
def add_todo():
    current_todo = Text_Field.get()
    lb_tasks.insert(lb_tasks.size(), current_todo)
    Text_Field.delete(0, ctk.END)

def del_todo():
    current_todo = lb_tasks.curselection()
    lb_tasks.delete(current_todo)

def clear_listbox():
    lb_tasks.delete('all')

def move_down():
    current_todo = lb_tasks.curselection()
    lb_tasks.move_down(current_todo)
    
def move_up():
    current_todo = lb_tasks.curselection()
    lb_tasks.move_up(current_todo)
    
def modify():
    current_todo = Text_Field.get()
    current_index = lb_tasks.curselection()
    #lb_tasks.delete(current_index)
    lb_tasks.insert(current_index,option = current_todo)
    #lb_tasks.delete(current_index)
    Text_Field.delete(0, ctk.END)
    

title_label = ctk.CTkLabel(root, text="Tasks' List", font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=20, pady=(40, 20))

sub_title_label = ctk.CTkLabel(root, text='"Today\'s TO-DOs are Tomorrow\'s Triumph"', font=ctk.CTkFont(size=20, weight="bold"))
sub_title_label.pack(padx=10, pady=(0, 20))

lb_tasks = CTkListbox(root, width=500, height=200)
lb_tasks.pack()

Text_Field = ctk.CTkEntry(root, width=500, height=50, placeholder_text="Add todo")
Text_Field.pack(pady=(10, 10))

add_button = ctk.CTkButton(root, text="Add", width=500, command=add_todo)
add_button.pack(pady=10)

del_button = ctk.CTkButton(root, text="Delete Task", width=500, command=del_todo)
del_button.pack(pady=10)

del_button = ctk.CTkButton(root, text="Delete All", width=500, command=clear_listbox)
del_button.pack()

Move = ctk.CTkFrame(root)
Move.pack(pady = 10)

move_up_button = ctk.CTkButton(Move, text="Move up" , command=move_up)
move_up_button.grid(row=0 , column = 0)
move_down_button = ctk.CTkButton(Move, text="Move Down", command=move_down)
move_down_button.grid(row=0 , column = 1)
modify_btn = ctk.CTkButton(Move, text="Modify", command=modify)
modify_btn.grid(row=0 , column = 2)

root.mainloop()
