import tkinter as tk
from tkinter.constants import CURRENT, DISABLED
from FunKey import GetCoor
#import Mode
# import numpy as np

#widget
root = tk.Tk()

#light/dark mode
global MyFg; MyFg = "#ffffff"
global MyBg; MyBg = "#000000"
global MyBg2; MyBg2 = "#888888"

#input
e = tk.Entry(root, bd = 2, width = 30, fg = MyFg, bg = MyBg)
e.grid(row = 0, column = 0, columnspan= 4)
e.insert(0, "0")

#Functioning of arithmetic operators

def Fun(function):
    #global LastFun; LastFun = function
    #global operation; operation = False

    #assigns operator
    if function in ["+","-","×","÷","^"]:
        global operation; operation = function
        global Num1; Num1 = float(e.get())
        e.delete(0, tk.END)

    #performs calculation
    if function == "=":
        if e.get() == "":
            pass
        else:
            global Num2; Num2 = float(e.get())
            e.delete(0, tk.END)
        try:
            if operation == "+":
                e.insert(0, Num1+Num2)
            elif operation == "-":
                e.insert(0, Num1-Num2)
            elif operation == "×":
                e.insert(0, Num1*Num2)
            elif operation == "÷":
                e.insert(0, Num1/Num2)
            elif operation == "^":
                e.insert(0, Num1**Num2)

        except NameError as Err:
            e.insert(0, e.get())

    #clears everything
    if function == "CE":
        e.delete(0, tk.END)

    #backspace
    if function == "←":
        temp = e.get()
        e.delete(0, tk.END)
        e.insert(0, temp[0:-1])
    
    # if function == "←":
    #     temp = e.get()
    #     e.delete(0, tk.END)
    #     e.insert(0, )

#Insert numbers
def Num(number):
    """Inserts a number at the end of the string in textbox

    Args:
        number (string): Values from 0 to 9 and "." 
    """
    if number == ".":
        if e.get().count(".") == 0:
            e.insert(tk.END, str(number))

    elif e.get() == "0":
        e.delete(0, tk.END)
        e.insert(tk.END, str(number))
    elif e.get() == "":
        #e.delete(0, tk.END)
        e.insert(0, str(number))
    
    
    else: e.insert(tk.END, str(number))


#Buttons creation
Button = {}
Nums = list(range(0,10))
Funs = ["+","-","×","÷","^","=",".","←","CE"]

#Buttons declaration
if True:
    Button[0] = tk.Button(root, text = 0, fg = MyFg, bg = MyBg, padx = 20, pady = 15, command = lambda: Num(0))
    Button["."] = tk.Button(root, text = ".", fg = MyFg, bg = MyBg, padx = 20, pady = 15, command = lambda: Num("."))#, state= tk.DISABLED)

    Button[1] = tk.Button(root, text = 1, fg = MyFg, bg = MyBg, padx = 20, pady = 15, command = lambda: Num(1))
    Button[2] = tk.Button(root, text = 2, fg = MyFg, bg = MyBg, padx = 20, pady = 15, command = lambda: Num(2))
    Button[3] = tk.Button(root, text = 3, fg = MyFg, bg = MyBg, padx = 20, pady = 15, command = lambda: Num(3))

    Button[4] = tk.Button(root, text = 4, fg = MyFg, bg = MyBg, padx = 20, pady = 15, command = lambda: Num(4))
    Button[5] = tk.Button(root, text = 5, fg = MyFg, bg = MyBg, padx = 20, pady = 15, command = lambda: Num(5))
    Button[6] = tk.Button(root, text = 6, fg = MyFg, bg = MyBg, padx = 20, pady = 15, command = lambda: Num(6))

    Button[7] = tk.Button(root, text = 7, fg = MyFg, bg = MyBg, padx = 20, pady = 15, command = lambda: Num(7))
    Button[8] = tk.Button(root, text = 8, fg = MyFg, bg = MyBg, padx = 20, pady = 15, command = lambda: Num(8))
    Button[9] = tk.Button(root, text = 9, fg = MyFg, bg = MyBg, padx = 20, pady = 15, command = lambda: Num(9))

    Button["+"] = tk.Button(root, text = "+", fg = MyFg, bg = MyBg2, padx = 20, pady = 15, command = lambda: Fun("+"))
    Button["-"] = tk.Button(root, text = "-", fg = MyFg, bg = MyBg2, padx = 20, pady = 15, command = lambda: Fun("-"))
    Button["×"] = tk.Button(root, text = "×", fg = MyFg, bg = MyBg2, padx = 20, pady = 15, command = lambda: Fun("×"))
    Button["÷"] = tk.Button(root, text = "÷", fg = MyFg, bg = MyBg2, padx = 20, pady = 15, command = lambda: Fun("÷"))
    Button["^"] = tk.Button(root, text = "^", fg = MyFg, bg = MyBg2, padx = 20, pady = 8, command = lambda: Fun("^"))
    
    Button["="] = tk.Button(root, text = "=", fg = MyFg, bg = MyBg2, padx = 20, pady = 15, command = lambda: Fun("="))
    Button["←"] = tk.Button(root, text = "←", fg = MyFg, bg = MyBg2, padx = 20, pady = 8, command = lambda: Fun("←"))
    Button["CE"] = tk.Button(root, text = "CE", fg = MyFg, bg = MyBg2, padx = 20, pady = 8, command = lambda: Fun("CE"))

#Buttons in grid
for i in Nums + Funs:
    
    iRow, iCol = GetCoor(obj = i)
    Button[i].grid(row = iRow, column = iCol)

root.mainloop()