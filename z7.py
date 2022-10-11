import sys
from tkinter import *
from tkinter import ttk
import time
from datetime import datetime

now = datetime.now()
x = []
d = {}


def quit():
    print("Have a great day! Goodbye :)")
    sys.exit(0)


def display():
    x = []
    for key, value in d.items():
        x.append([key, value])
    print(x)
    x_var.set(x)


def add(*args):
    global stock
    global d
    global Quantity
    stock = stock_Entry.get()
    Quantity = int(Quantity_Entry.get())
    if stock not in d:
        d[stock] = Quantity
    else:
        d[stock] += Quantity


root = Tk()
root.title("Homework 5 216020088")

x_var = StringVar()
x_var.set(x)

mainframe = ttk.Frame(root, padding="6 6 20 20")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

ttk.Label(mainframe, text="you are accesing this on day %s of month %s of %s" % (
    now.day, now.month, now.year) + " at exactly %s:%s:%s" % (now.hour, now.minute, now.second), foreground="yellow",
          background="Black").grid(column=0, row=0)

stock_Entry = ttk.Entry(mainframe, width=60, textvariable="stock")
stock_Entry.grid(column=0, row=1, sticky=W)
ttk.Label(mainframe, text="Please enter the stock name").grid(column=1, row=1, sticky=(N, W, E, S))

Quantity_Entry = ttk.Entry(mainframe, width=60, textvariable="Quantity")
Quantity_Entry.grid(column=0, row=2, sticky=W)
ttk.Label(mainframe, text="Please enter the quantity").grid(column=1, row=2, sticky=(N, W, E, S))

ttk.Button(mainframe, text="Add", command=add).grid(column=0, row=3, sticky=W)
ttk.Button(mainframe, text="Display", command=display).grid(column=0, row=3, sticky=S)
ttk.Button(mainframe, text="Exit", command=quit).grid(column=0, row=3, sticky=E)

ttk.Label(mainframe, textvariable=x_var).grid(column=0, row=4, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
root.mainloop()
