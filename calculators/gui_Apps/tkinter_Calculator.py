from tkinter import *

root = Tk()
root.title("Calculator")
root.resizable(0,0)
root.iconbitmap('img/calculator.ico')
root.config(bg="black")

#Lista de botones
btn_list = [
    '7', '8', '9', '+', 
    '4', '5', '6', '-', 
    '1', '2', '3', '*', 
    '0', 'C', '=', '/', 
    '.', '(', ')', '%', 
    '√'
    ]

#Creacion de botones
def btn_create(value):
    btn = Button(root, text=value, font=("arial", 20, "bold"), width=5, height=2, command=lambda:click_btn(value))
    return btn

#Renderizado de botones
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

#Funciones
def click_btn(value):
    text = str(value)
    if text.isnumeric():
        number_inside = int(text)
        if number_inside >= 0 and number_inside <= 9:
            global number
            number += text
            update(number)
    if text == '+' or text == '-' or text == '*' or text == '/' or text == '%':
        global operator
        operator = text
        number = ""
        update(operator)
    if text == '=':
        calculate(int(number), operator)
    if text == 'C':
        clear()

def calculate(number, operator):
    result = 0
    match(operator):
        case '+':
            result += number
            update(result)
        case '-':
            result -= number
            update(result)
        case '*':
            result *= number
            update(result)
        case '/':
            result /= number
            update(result)
        case '%':
            result %= number
            update(result)


def clear():
    clean_box = ""
    update(clean_box)

def update(value):
    text.set(value)

def equal():
    global operator
    try:
        result = eval(operator)
        operator = str(result)
        text.set(result)
    except:
        text.set("Error")
        operator = ""

def square_root():
    global operator
    try:
        result = eval(operator)
        operator = str(result)
        text.set(result)
    except:
        text.set("Error")
        operator = ""

#Pantalla
screen = Entry(root, font=("arial", 20, "bold"), width=22, borderwidth=10, background="black", fg="white", textvariable=text)
screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#Ejecucion
root.mainloop()
