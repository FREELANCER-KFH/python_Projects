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
    btn = Button(root, text=value, font=("arial", 20, "bold"), width=5, height=2, command=lambda:click_btn(value))
    return btn

#Grid
i = 0
for row in range(1, 6):
    for column in range(4):
        btn = btn_create(btn_list[i])
        btn.grid(row=row, column=column, padx=5, pady=5)
        i += 1

#Variables
    operator = ""
    number = ""
    text = StringVar()
    container = ""
    result = 0

#Click
def click_btn(value):
    global number
    global operator
    global container
    text = str(value)
    if text.isnumeric():
        text = int(text)
        if (text >= 0 and text <= 9):
            number += str(text)
            container = number
            update(number)
    elif text == '.' or text == '(' or text == ')':
        number += text
        update(number)
    else:
        if text == '+' or text == '-' or text == '*' or text == '/' or text == '%':
            operator = text
            update(operator)
            number = ""
        elif text == '=':
            update(calculate(int(container), operator))
            number = ""
            operator = ""
        elif text == 'C':
            clear()

#Calculate
def calculate(current, op):
    global result
    match(op):
        case '+':
            result += current
            return result
        case '-':
            result -= current
            return result
        case '*':
            result *= current
            return result
        case '/':
            result /= current
            return result
        case '%':
            result %= current
            return result

#Clear
def clear():
    global operator
    global result
    global number
    number = ""
    operator = ""
    result = 0
    update(number)

#Update
def update(value):
    text.set(value)

#Equal
def equal():
    global operator
    try:
        result = eval(operator)
        operator = str(result)
        text.set(result)
    except:
        text.set("Error")
        operator = ""

#Square root
def square_root():
    global operator
    try:
        result = eval(operator)
        operator = str(result)
        text.set(result)
    except:
        text.set("Error")
        operator = ""

#Screen
screen = Entry(root, font=("arial", 20, "bold"), width=22, borderwidth=10, background="black", fg="white", textvariable=text)
screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#Loop
root.mainloop()
