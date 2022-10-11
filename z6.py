import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

z1 = []
filepath = askopenfilename
mylist = []

def open_file():
    global filepath, mylist
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


def save_file(mylist):
    global filepath
    # записываем изменения
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        output_file.writelines([str(i) for i in mylist])
    output_file.close()
    # перечитываем файл, чтобы отобразить изменения
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)



# подготавливает к записи нужные подсчитанные строки
def savedata():
    for i in range(7, 15):
        mylist[i] = mylist[i].strip('\n')
        print("беру ", mylist[i], " и вношу туда \n", mylist[i] + str(z1[i - 1]) + "р.")
        mylist[i] = mylist[i] + str(z1[i - 1]) + " р.\n"
    print(mylist)
    save_file(mylist)

# сумма стр. 1–9
def str10():
    total = 0
    for i in range(0, 8):
        total = total + z1[i]
    return total


# подсчет необходимых частей
def calculate():
    global z1
    z1.append(z1[5] * 35 / 100)
    z1.append(z1[5] / 100)
    z1.append(z1[5] * 4 / 100)
    z1.append(str10())
    z1.append(z1[9] * 5 / 100)
    z1.append(z1[9] + z1[10])
    z1.append(z1[11] * 20 / 100)
    z1.append(z1[11] + z1[12])
    print(z1)


# запись значений в память для вычислений
def to_memory(mylist):
    global z1
    print(mylist)
    for i in range(1, 7):
        z1.append(float(extractor(mylist[i])))
    calculate()


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
btn_save = tk.Button(frm_buttons, text="РАСЧЕТ", command=savedata)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
