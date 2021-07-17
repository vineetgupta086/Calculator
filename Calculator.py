import tkinter as tk
from FunKey import GetCoor, GetFun
import Mode
# import numpy as np

#widget
root = tk.Tk()

#light/dark mode
MyFg = "#ffffff"
MyBg = "#000000"

#input
e = tk.Entry(root, width = 30, fg = MyFg, bg = MyBg)
e.grid(row = 0, column = 0, columnspan= 4)

#Button Functions
def Num():
    pass

def Fun():
    pass

#Buttons
Button = {}
Nums = list(range(0,10))
Funs = ["+","-","×","÷","=","."]

for i in Nums + Funs:
    if isinstance(i,int):
        Button[i] = tk.Button(root, text = i, fg = MyFg, bg = MyBg, padx = 20, pady = 15, command = Num)
    else:
        Button[i] = tk.Button(root, text = i, fg = MyFg, bg = MyBg, padx = 20, pady = 15, command = Fun)
    iRow, iCol = GetCoor(obj = i)
    Button[i].grid(row = iRow+1, column = iCol)

root.mainloop()