from tkinter import *

root = Tk()
root.title("Calculator")
root.resizable(0,0)
root.iconbitmap('img/calculator.ico')
root.config(bg="black")

#Variables
operator = ""
text = StringVar()

#Funciones
def click_btn(value):
    global operator
    operator += str(value)
    text.set(operator)

def borrar():
    global operator
    operator = ""
    text.set("")
    screen.update()

def calcular():
    global operator
    try:
        r = str(eval(operator))
    except:
        r = "Error"
    text.set(r)
    operator = ""

#Pantalla
screen = Entry(root, font=("arial", 20, "bold"), width=22, borderwidth=10, background="black", fg="white", textvariable=text)
screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#Botones
btn_1 = Button(root, text="1", font=("arial", 20, "bold"), width=5, height=2, command=lambda:click_btn(1))
btn_2 = Button(root, text="2", font=("arial", 20, "bold"), width=5, height=2, command=lambda:click_btn(2))
btn_3 = Button(root, text="3", font=("arial", 20, "bold"), width=5, height=2, command=lambda:click_btn(3))
btn_4 = Button(root, text="4", font=("arial", 20, "bold"), width=5, height=2, command=lambda:click_btn(4))
btn_5 = Button(root, text="5", font=("arial", 20, "bold"), width=5, height=2, command=lambda:click_btn(5))
btn_6 = Button(root, text="6", font=("arial", 20, "bold"), width=5, height=2, command=lambda:click_btn(6))
btn_7 = Button(root, text="7", font=("arial", 20, "bold"), width=5, height=2, command=lambda:click_btn(7))
btn_8 = Button(root, text="8", font=("arial", 20, "bold"), width=5, height=2, command=lambda:click_btn(8))
btn_9 = Button(root, text="9", font=("arial", 20, "bold"), width=5, height=2, command=lambda:click_btn(9))
btn_0 = Button(root, text="0", font=("arial", 20, "bold"), width=5, height=2, command=lambda:click_btn(0))
btn_suma = Button(root, text="+", font=("arial", 20, "bold"), width=5, height=2, command=lambda:click_btn("+"))
btn_resta = Button(root, text="-", font=("arial", 20, "bold"), width=5, height=2, command=lambda:click_btn("-"))
btn_multi = Button(root, text="*", font=("arial", 20, "bold"), width=5, height=2, command=lambda:click_btn("*"))
btn_div = Button(root, text="/", font=("arial", 20, "bold"), width=5, height=2, command=lambda:click_btn("/"))
btn_mod = Button(root, text="%", font=("arial", 20, "bold"), width=5, height=2, command=lambda:click_btn("%"))
btn_pot = Button(root, text="^", font=("arial", 20, "bold"), width=5, height=2, command=lambda:click_btn("**"))
btn_raiz = Button(root, text="√", font=("arial", 20, "bold"), width=5, height=2, command=lambda:click_btn("**0.5"))
btn_igual = Button(root, text="=", font=("arial", 20, "bold"), width=5, height=2, command=calcular)
btn_borrar = Button(root, text="C", font=("arial", 20, "bold"), width=5, height=2, command=borrar)

#Posicion de los botones
btn_1.grid(row=3, column=0, padx=5, pady=5)
btn_2.grid(row=3, column=1, padx=5, pady=5)
btn_3.grid(row=3, column=2, padx=5, pady=5)
btn_4.grid(row=2, column=0, padx=5, pady=5)
btn_5.grid(row=2, column=1, padx=5, pady=5)
btn_6.grid(row=2, column=2, padx=5, pady=5)
btn_7.grid(row=1, column=0, padx=5, pady=5)
btn_8.grid(row=1, column=1, padx=5, pady=5)
btn_9.grid(row=1, column=2, padx=5, pady=5)
btn_0.grid(row=4, column=1, padx=5, pady=5)
btn_suma.grid(row=1, column=3, padx=5, pady=5)
btn_resta.grid(row=2, column=3, padx=5, pady=5)
btn_multi.grid(row=3, column=3, padx=5, pady=5)
btn_div.grid(row=4, column=3, padx=5, pady=5)
btn_mod.grid(row=4, column=0, padx=5, pady=5)
btn_pot.grid(row=4, column=2, padx=5, pady=5)
btn_raiz.grid(row=5, column=0, padx=5, pady=5)
btn_igual.grid(row=5, column=1, padx=5, pady=5)
btn_borrar.grid(row=5, column=2, padx=5, pady=5)

root.mainloop()
