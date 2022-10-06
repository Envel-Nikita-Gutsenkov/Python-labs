import tkinter as tk

m1 = "1. Отсортировать массив по невозрастанию методом включения с выбором включаемого\n элемента справа налево"
m2 = "2. Отсортировать массив по невозрастанию методом извлечения максимального элемента,\n поиск максимального элемента проводить слева направо"
m3 = "3. Отсортировать массив по неубыванию методом обменов рядом стоящих элементов с\n фиксированным числом просмотров, направленных справа налево"
m4 = "4. Отсортировать массив по невозрастанию методом обменов рядом стоящих элементов\n с минимально необходимым (переменным) числом просмотров, направленных слева направо"
m5 = "5. Отсортировать массив по неубыванию методом обменов рядом стоящих элементов за\n один просмотр (с возвратами) справа налево"
m6 = "6. Получить упорядоченный по неубыванию массив методом слияния двух упорядоченных\n по невозрастанию массивов"
m7 = "7. Отсортировать массив по невозрастанию методом распределения по массиву ключей,\n упорядоченному по неубыванию"


# ЛОГИКА

# методы сортировки
def one():
    for f in range(len(a1) - 1, -1, -1):
        for u in range(len(a1) - 1, -1, -1):
            if a1[f] < a1[u]:
                swapPositions(f, u)
    output()


def two():
    for f in range(0, len(a1), 1):
        temp = f
        for u in range(f + 1, len(a1), 1):
            if a1[temp] < a1[u]:
                temp = u
        swapPositions(f, temp)
    output()


def three():
    for u in range(len(a1) - 1, 0, -1):
        for f in range(len(a1) - 1, 0, -1):
            if a1[f - 1] > a1[f]:
                swapPositions(f - 1, f)
    output()


def four():
    w = bool(True)
    for u in range(1, len(a1), 1):
        if w == bool(False):
            return output()
        else:
            w = bool(False)
            for f in range(1, len(a1), 1):
                if a1[f - 1] < a1[f]:
                    swapPositions(f - 1, f)
                    w = bool(True)
    output()


def five():
    for u in range(len(a1) - 1, 0, -1):
        w = bool(True)
        for f in range(len(a1) - 1, 0, -1):
            if w == bool(False):
                return
            elif a1[f - 1] > a1[f]:
                swapPositions(f - 1, f)
                print("Произвел замену и возврат к началу")
                output()
                w = bool(False)
    output()


def six():
    output()


def seven():
    output()


# вывод данных
def output():
    print("Результат: ")
    print(None)


# ИНТЕРФЕЙС
window = tk.Tk()
window.title("Лабораторная работа 5")

#window.rowconfigure(0, minsize=800, weight=1)
#window.columnconfigure(1, minsize=800, weight=1)

# Create the label objects and pack them using grid
tk.Label(window, text="Выберите способ сортировки").grid(row=0, column=0)

frm_buttons = tk.Frame(window)
btn1 = tk.Button(frm_buttons, text=m1, command=one)
btn2 = tk.Button(frm_buttons, text=m2, command=two)
btn3 = tk.Button(frm_buttons, text=m3, command=three)
btn4 = tk.Button(frm_buttons, text=m4, command=four)
btn5 = tk.Button(frm_buttons, text=m5, command=five)
btn6 = tk.Button(frm_buttons, text=m6, command=six)
btn7 = tk.Button(frm_buttons, text=m7, command=seven)

btn1.grid(row=2, column=2, sticky="ew", padx=5, pady=5)
btn2.grid(row=3, column=2, sticky="ew", padx=5, pady=5)
btn3.grid(row=4, column=2, sticky="ew", padx=5, pady=5)
btn4.grid(row=5, column=2, sticky="ew", padx=5, pady=5)
btn5.grid(row=6, column=2, sticky="ew", padx=5, pady=5)
btn6.grid(row=7, column=2, sticky="ew", padx=5, pady=5)
btn7.grid(row=8, column=2, sticky="ew", padx=5)

frm_buttons.grid(row=0, column=1, sticky="ns")

window.mainloop()