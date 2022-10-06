import tkinter as tk

# Create the master object
master = tk.Tk()

# Create the label objects and pack them using grid
tk.Label(master, text="Выберите способ сортировки").grid(row=0, column=0)


button1 = tk.Button(master, text="Button 1")
button1.grid(columnspan=2, row=2, column=0)

# Create another button
button2 = tk.Button(master, text="Button 2")
button2.grid(columnspan=1, row=2, column=2)

# The mainloop
tk.mainloop()