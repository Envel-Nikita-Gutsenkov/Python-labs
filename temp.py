'''import tkinter as tk

# Create the master object
master = tk.Tk()

# Create the label objects and pack them using grid
tk.Label(master, text="Выберите способ сортировки").grid(row=0, column=0)


button1 = tk.Button(master, text="Button 1")
button1.grid(columnspan=2, row=2, column=0)

# Create another button
button2 = tk.Button(master, text="Button 2")
button2.grid(columnspan=4, row=4, column=0)

# The mainloop
tk.mainloop()
import tkinter as tk

window = tk.Tk()

for i in range(10):
        frame = tk.Frame(master=window)
        frame.grid(row=i, column=1, padx=5, pady=5)
        label = tk.Entry(master=frame, width=10)
        label2 = tk.Label(master=frame, text=f"Элемент номер {i}")
        label.pack(padx=5, pady=5)
        label2.pack(padx=5, pady=5)

window.mainloop()'''

from tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set )
for line in range(100):
   mylist.insert(END, "This is line number " + str(line))

mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

mainloop()
