# Calculator with tkinter
# Version: 1.0.0
# Autor: Kevin Feliz Henriquez
# Github: https://github.com/FREELANCER-KFH
# Date: 01/05/2024
# Python version: 3.9.6
# Tkinter version: 8.6
# License: MIT
# Editor: Visual Studio Code (https://code.visualstudio.com/)


#Import
from tkinter import *

#functions
def btn_click(value):
    if value == "=":
        try:
            result = eval(txt_Entry.get())
            txt_Entry.delete(0, END)
            txt_Entry.insert(0, result)
        except:
            txt_Entry.delete(0, END)
            txt_Entry.insert(0, "Error")
    elif value == "C":
        txt_Entry.delete(0, END)
    elif value == "√":
        try:
            result = eval(txt_Entry.get())
            txt_Entry.delete(0, END)
            txt_Entry.insert(0, result ** 0.5)
        except:
            txt_Entry.delete(0, END)
            txt_Entry.insert(0, "Error")
    else:
        txt_Entry.insert(END, value)

def txt_show(value):
    if value == 0:
        return "0"
    else:
        return value

#Window
root = Tk()
root.title("Calculator")
root.resizable(0,0)
root.iconbitmap('img/calculator.ico')
root.config(bg="black")

#Buttons list
btn_list = [
    '7', '8', '9', '+', 
    '4', '5', '6', '-', 
    '1', '2', '3', '*', 
    '0', 'C', '=', '/', 
    '.', '(', ')', '%', 
    '√'
    ]

#Buttons
def btn_create(value):
    btn = Button(root, text=value, font=("arial", 20, "bold"), width=5, height=2, borderwidth=5, background="black", fg="white", command=lambda: btn_click(value))
    return btn

#Grid
i = 0
for row in range(1, 6):
    for column in range(4):
        btn = btn_create(btn_list[i])
        btn.grid(row=row, column=column, padx=5, pady=5)
        i += 1

#Screen
txt_Entry = Entry(root, font=("arial", 20, "bold"), width=22, borderwidth=10, background="black", fg="white", textvariable=txt_show(0))
txt_Entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#Loop
root.mainloop()
