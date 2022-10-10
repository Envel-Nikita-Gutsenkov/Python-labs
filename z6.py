import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

z1 = [14]


def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
        input_file.seek(0)
        mylist = input_file.readlines()
    window.title(f"{filepath}")
    to_memory(mylist)


def save_file():
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"{filepath}")


def calculate():
    None
    #


# запись значений в память для вычислений
def to_memory(mylist):
    z1 = [14]
    print(mylist)
    for i in range(1, 7, 1):
        print("шаг ", i, "запись в ", i-1)
        print("элемент " + mylist[i])
        z1[i-1] = extractor(mylist[i])


# получает строку и извлекает из нее значение, используя разделитель | и поиск цифр
def extractor(pstring):
    res = pstring.split("|", 2)
    splitting = res[2]
    result = ""
    for m in splitting:
        if m.isdigit():
            result = result + m
    print("Получил число путем извлечения: " + result)
    return result


window = tk.Tk()
window.title("Лабораторная работа 6")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(frm_buttons, text="Открыть", command=open_file)
btn_save = tk.Button(frm_buttons, text="РАСЧЕТ", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
