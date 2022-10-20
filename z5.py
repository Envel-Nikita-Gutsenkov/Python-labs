import tkinter as tk

m1 = "1. Отсортировать массив по невозрастанию методом включения с выбором включаемого\n элемента справа налево"
m2 = "2. Отсортировать массив по невозрастанию методом извлечения максимального элемента,\n поиск максимального элемента проводить слева направо"
m3 = "3. Отсортировать массив по неубыванию методом обменов рядом стоящих элементов с\n фиксированным числом просмотров, направленных справа налево"
m4 = "4. Отсортировать массив по невозрастанию методом обменов рядом стоящих элементов\n с минимально необходимым (переменным) числом просмотров, направленных слева направо"
m5 = "5. Отсортировать массив по неубыванию методом обменов рядом стоящих элементов за\n один просмотр (с возвратами) справа налево"
m6 = "6. Получить упорядоченный по неубыванию массив методом слияния двух упорядоченных\n по невозрастанию массивов"
m7 = "7. Отсортировать массив по невозрастанию методом распределения по массиву ключей,\n упорядоченному по неубыванию"

a1 = []
a2 = []
smethod = ""


# ЛОГИКА

# методы сортировки
# Отсортировать массив по невозрастанию методом включения с выбором включаемого элемента справа налево
def one(window):
    global a1, smethod
    smethod = m1
    for f in range(len(a1) - 1, -1, -1):
        for u in range(len(a1) - 1, -1, -1):
            if a1[f] < a1[u]:
                a1[f], a1[u] = a1[u], a1[f]
    # выводим массивы
    switch(window, output, None)


# Отсортировать массив по невозрастанию методом извлечения максимального элемента, поиск максимального элемента проводить слева направо
def two(window):
    global a1, smethod
    smethod = m2
    for f in range(0, len(a1), 1):
        temp = f
        for u in range(f + 1, len(a1), 1):
            if a1[temp] < a1[u]:
                temp = u
        a1[f], a1[temp] = a1[temp], a1[f]
    # выводим массивы
    switch(window, output, None)


# Отсортировать массив по неубыванию методом обменов рядом стоящих элементов с фиксированным числом просмотров, направленных справа налево
def three(window):
    global a1, smethod
    smethod = m3
    for u in range(len(a1) - 1, 0, -1):
        for f in range(len(a1) - 1, 0, -1):
            if a1[f - 1] > a1[f]:
                a1[f], a1[f - 1] = a1[f - 1], a1[f]
    # выводим массивы
    switch(window, output, None)


# Отсортировать массив по невозрастанию методом обменов рядом стоящих элементов с минимально необходимым (переменным) числом просмотров, направленных слева направо
def four(window):
    global a1, smethod
    smethod = m4
    # для выполнения первой интерации
    w = bool(True)
    for u in range(1, len(a1), 1):
        # если в предыдущей интерации действий не было, завершить
        if w == bool(False):
            return switch(window, output, None)
        else:
            w = bool(False)
            for f in range(1, len(a1), 1):
                if a1[f - 1] < a1[f]:
                    a1[f], a1[f - 1] = a1[f - 1], a1[f]
                    w = bool(True)
    # выводим массивы
    switch(window, output, None)


# Отсортировать массив по неубыванию методом обменов рядом стоящих элементов за один просмотр (с возвратами) справа налево
def five(window):
    global a1, smethod
    smethod = m5
    left, right = 0, len(a1) - 1
    # сравниваем элементы попарно и меняем при необходимости
    while left <= right:
        for i in range(left, right, +1):
            if a1[i] > a1[i + 1]:
                a1[i], a1[i + 1] = a1[i + 1], a1[i]
        right -= 1
        for i in range(right, left, -1):
            if a1[i - 1] > a1[i]:
                a1[i], a1[i - 1] = a1[i - 1], a1[i]
        left += 1
    # выводим массивы
    switch(window, output, None)


# Получить упорядоченный по неубыванию массив методом слияния двух упорядоченных по невозрастанию массивов
def six(window):
    global a1, smethod
    smethod = m6
    '''# делим массив на 2 массива
    L, R = a1[:len(a1) // 2], a1[len(a1) // 2:]
    # сортируем оба массива по невозрастанию
    L.sort(reverse=True)
    R.sort(reverse=True)'''
    mergeSort(0, len(a1) - 1)
    switch(window, output, None)


def mergeSort(l, r):
    if l < r:
        m = (l + r) // 2

        mergeSort(l, m)
        mergeSort(m + 1, r)
        merge(l, m, r)


def merge(l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        L[i] = a1[l + i]

    for j in range(0, n2):
        R[j] = a1[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            a1[k] = L[i]
            i += 1
        else:
            a1[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        a1[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        a1[k] = R[j]
        j += 1
        k += 1


# Отсортировать массив по невозрастанию методом распределения по массиву ключей, упорядоченному по неубыванию
def seven(window):
    global a1, smethod
    smethod = m7
    a1.sort(reverse=True)
    end, marker, i = len(a1) - 1, 0, 0

    while i <= end:
        if a1[i] >= a1[end]:
            a1[marker], a1[i] = a1[i], a1[marker]
            marker += 1
        i += 1

    switch(window, output, None)


# получает строку данных из tk.Entry и создает из этого массив
def arrayprocess(rawarray):
    global a1, a2
    a1 = rawarray.split(',')
    # преобразование str в int
    for i in range(len(a1)):
        a1[i] = int(a1[i])
    # для вывода исходного массива в ответе
    a2 = list(a1)
    method()


# ИНТЕРФЕЙС

# управляет переключением интерфейса, чтобы одновременно существовал только один интерфейс
def switch(interface, newinterface, data):
    interface.destroy()
    if newinterface is not None and data is not None:
        newinterface(data)
    elif newinterface is not None and data is None:
        newinterface()


# выбор метода сортировки
def method():
    window = tk.Tk()
    window.title("Лабораторная работа 5")

    window.geometry("685x455")

    frm_buttons = tk.Frame(window)
    tk.Label(frm_buttons, text="Выберите способ сортировки", font=('Helvetica', 16, "bold")).grid(row=0, column=0)
    btn1 = tk.Button(frm_buttons, text=m1, command=lambda: one(window))
    btn2 = tk.Button(frm_buttons, text=m2, command=lambda: two(window))
    btn3 = tk.Button(frm_buttons, text=m3, command=lambda: three(window))
    btn4 = tk.Button(frm_buttons, text=m4, command=lambda: four(window))
    btn5 = tk.Button(frm_buttons, text=m5, command=lambda: five(window))
    btn6 = tk.Button(frm_buttons, text=m6, command=lambda: six(window))
    btn7 = tk.Button(frm_buttons, text=m7, command=lambda: seven(window))

    btn1.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
    btn2.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
    btn3.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
    btn4.grid(row=5, column=0, sticky="ew", padx=5, pady=5)
    btn5.grid(row=6, column=0, sticky="ew", padx=5, pady=5)
    btn6.grid(row=7, column=0, sticky="ew", padx=5, pady=5)
    btn7.grid(row=8, column=0, sticky="ew", padx=5)

    frm_buttons.grid(row=0, column=1, sticky="ns")

    window.mainloop()


# ввод элементов массива
def arrayinput():
    window = tk.Tk()
    window.title("Лабораторная работа 5")
    window.geometry("685x455")

    fields = {}
    rawarray = tk.StringVar()

    fields['array_label'] = tk.Label(text="Введите элементы массива через запятую", font=('Helvetica', 18, "bold"))
    fields['rawarray'] = tk.Entry(window, textvariable=rawarray)

    for field in fields.values():
        field.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

    tk.Button(text='OK', width=15, command=lambda: (switch(window, arrayprocess, rawarray.get()))).pack()

    window.mainloop()


#  Вывод ответа
def output():
    window = tk.Tk()
    window.title("Лабораторная работа 5")
    window.geometry("685x455")

    tk.Label(window, text="Задача выполнена", font=('Helvetica', 16, "bold")).pack()

    text = tk.Text(window, height=10, font=('Helvetica', 18))
    text.pack()

    # исключаем переход на новую строку
    methodoutput = smethod.replace('\n',"")

    text.insert('1.0', 'Был введен массив:\n')
    text.insert('2.0', a2)
    text.insert('4.0', '\nИспользовался метод сортировки:\n')
    text.insert('5.0', methodoutput)
    text.insert('7.0', '\nРезультат после сортировки:\n')
    text.insert('8.0', a1)

    tk.Button(text='Закрыть программу', width=15, command=lambda: (switch(window, None, None))).pack()

    # read only
    text.configure(state='disabled')

    window.mainloop()


arrayinput()
