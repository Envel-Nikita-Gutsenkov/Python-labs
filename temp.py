from tkinter import *
from tkinter import ttk

'''d = {
    "1": {
        "udk": "1",
        "k_name": "Name1",
        "k_genre": "Genre1",
        "manufacturer": "Manuf1",
        "release_year": 2000,
        "out_date": "01.01",
        "out_time": "10.02"
    },
    "2": {
        "udk": "1",
        "k_name": "Name1",
        "k_genre": "Genre1",
        "manufacturer": "Manuf1",
        "release_year": 2000,
        "out_date": "01.01",
        "out_time": "10.02"
    },
    "3": {
        "udk": "1",
        "k_name": "Name1",
        "k_genre": "Genre1",
        "manufacturer": "Manuf1",
        "release_year": 2000,
        "out_date": "01.01",
        "out_time": "10.02"
    },
    "4": {
        "udk": "1",
        "k_name": "Name1",
        "k_genre": "Genre1",
        "manufacturer": "Manuf4",
        "release_year": 2000,
        "out_date": "01.01",
        "out_time": "10.02"
    }
}'''

d = {
        "udk": ["1","1","1"],
        "k_name": ["Name1","Name1","Name1"],
        "k_genre": ["Genre1","Genre1","Genre1"],
        "manufacturer": ["Manuf4","Manuf4","Manuf4"],
        "release_year": [2000,2000,2000],
        "out_date": ["01.01","01.01","01.01"],
        "out_time": ["10.02","10.02","10.02"]
}

count = 4

h1 = "УДК  кассеты"
h2 = "Название фильма"
h3 = "Жанр"
h4 = "Производитель"
h5 = "Год выпуска"
h6 = "Дата проката"
h7 = "Время проката"


# ЛОГИКА

def remove_record():
    global count

    set.insert(parent='', index='end', iid=count, text='',
               values=(udk.get(), k_name.get(), k_genre.get()))
    count += 1

    udk.delete(0, END)
    k_name.delete(0, END)
    k_genre.delete(0, END)


def input_record():
    '''set.insert(parent='', index='end', iid=count, text='',
               values=(udk.get(), k_name.get(), k_genre.get()))

    global count
    count+1'''
    global count
    count += 1
    #d[i] += 1

    d.add(str(count),'udk') #= toudk.get()
    d[str(count)]['k_name'] = tok_name.get()
    d[str(count)]['k_genre'] = tok_genre.get()
    d[str(count)]['manufacturer'] = tomanufacturer.get()
    d[str(count)]['release_year'] = torelease_year.get()
    d[str(count)]['out_date'] = toout_date.get()
    d[str(count)]['out_time'] = toout_time.get()

    print(d)

    toudk.delete(0, END)
    tok_name.delete(0, END)
    tok_genre.delete(0, END)
    tomanufacturer.delete(0, END)
    torelease_year.delete(0, END)
    toout_date.delete(0, END)
    toout_time.delete(0, END)

    tableupdate(count)

def tableupdate(i):
    main_menu.insert(parent='', index='end', iid=i - 1, text='', values=(
        d[str(i)]['udk'], d[str(i)]['k_name'], d[str(i)]['k_genre'], d[str(i)]['manufacturer'],
        d[str(i)]['release_year'],
        d[str(i)]['out_date'], d[str(i)]['out_time']))
    main_menu.pack()

# ИНТЕРФЕЙС

# основные функции
def additional_menu():
    ws2 = Tk()
    ws2.title('Лабораторная работа 7 - Основные функции')
    ws2.geometry('600x400')

    # удаление записей
    Label(ws2, text="Удаление всех записей с заданным", font=('Helvetica', 16, "bold")).pack()
    Input_frame = Frame(ws2)
    Input_frame.pack()

    # название
    release_year = Label(Input_frame, text=h5)
    release_year.grid(row=0, column=0)

    # столбец
    id_entry = Entry(Input_frame)
    id_entry.grid(row=1, column=0)

    Button(ws2, text="Удалить", command=input_record).pack()

    # заменить удк кассеты
    Label(ws2, text="Заменить УДК кассеты", font=('Helvetica', 16, "bold")).pack()
    Input_frame = Frame(ws2)
    Input_frame.pack()

    # названия
    k_name = Label(Input_frame, text=h2)
    k_name.grid(row=0, column=0)

    udk = Label(Input_frame, text=h1)
    udk.grid(row=0, column=1)

    udk_to = Label(Input_frame, text="Заменить УДК на")
    udk_to.grid(row=0, column=2)

    # столбцы
    k_name = Entry(Input_frame)
    k_name.grid(row=1, column=0)

    udk = Entry(Input_frame)
    udk.grid(row=1, column=1)

    udk_to = Entry(Input_frame)
    udk_to.grid(row=1, column=2)

    # кнопка добавить
    Input_button = Button(ws2, text="Применить", command=input_record)

    Input_button.pack()

    # все сведения по производителю
    Label(ws2, text="Все сведения о фильмах заданного", font=('Helvetica', 16, "bold")).pack()
    Input_frame = Frame(ws2)
    Input_frame.pack()

    manufacturer = Label(Input_frame, text=h4)
    manufacturer.grid(row=0, column=0)

    # столбец
    manufacturer = Entry(Input_frame)
    manufacturer.grid(row=1, column=0)

    Button(ws2, text="Показать", command=lambda: show_by_manufacturer(ws2)).pack()

    ws2.mainloop()


# все сведения по производителю (таблица)
def show_by_manufacturer(ws2):
    Label(ws2, text="Список записей", font=('Helvetica', 16, "bold")).pack()

    sbm_frame = Frame(ws2)
    sbm_frame.pack()

    # scrollbar
    sbm_scroll = Scrollbar(sbm_frame)
    sbm_scroll.pack(side=RIGHT, fill=Y)

    sbm_scroll = Scrollbar(sbm_frame, orient='horizontal')
    sbm_scroll.pack(side=BOTTOM, fill=X)

    sbm = ttk.Treeview(sbm_frame, yscrollcommand=sbm_scroll.set, xscrollcommand=sbm_scroll.set)
    # формат столбцов
    sbm.column("#0", width=0, stretch=NO)
    sbm.column("udk", anchor=CENTER, width=110)
    sbm.column("k_name", anchor=CENTER, width=140)
    sbm.column("k_genre", anchor=CENTER, width=90)
    sbm.column("release_year", anchor=CENTER, width=100)
    sbm.column("out_date", anchor=CENTER, width=100)
    sbm.column("out_time", anchor=CENTER, width=110)

    # названия столбцов
    sbm.heading("#0", text="", anchor=CENTER)
    sbm.heading("udk", text=h1, anchor=CENTER)
    sbm.heading("k_name", text=h2, anchor=CENTER)
    sbm.heading("k_genre", text=h3, anchor=CENTER)
    sbm.heading("release_year", text=h5, anchor=CENTER)
    sbm.heading("out_date", text=h6, anchor=CENTER)
    sbm.heading("out_time", text=h7, anchor=CENTER)

    # названия
    udk = Label(Input_frame, text=h1)
    udk.grid(row=0, column=0)

    k_name = Label(Input_frame, text=h2)
    k_name.grid(row=0, column=1)

    k_genre = Label(Input_frame, text=h3)
    k_genre.grid(row=0, column=2)

    release_year = Label(Input_frame, text=h5)
    release_year.grid(row=0, column=3)

    out_date = Label(Input_frame, text=h6)
    out_date.grid(row=0, column=4)

    out_time = Label(Input_frame, text=h7)
    out_time.grid(row=0, column=5)

    # столбцы
    udk = Entry(Input_frame)
    udk.grid(row=1, column=0)

    k_name = Entry(Input_frame)
    k_name.grid(row=1, column=1)

    k_genre = Entry(Input_frame)
    k_genre.grid(row=1, column=2)

    release_year = Entry(Input_frame)
    release_year.grid(row=1, column=3)

    out_date = Entry(Input_frame)
    out_date.grid(row=1, column=4)

    out_time = Entry(Input_frame)
    out_time.grid(row=1, column=5)

    # TODO delete
    sbm.insert(parent='', index='end', iid=0, text='',
               values=('1', 'Ninja', '101', 'Oklahoma', 'Moore'))


# основной интерфейс

ws = Tk()
ws.title('Лабораторная работа 7')
ws.geometry('1300x600')

Label(ws, text="Список записей", font=('Helvetica', 16, "bold")).pack()

main_frame = Frame(ws)
main_frame.pack()

# scrollbar
main_scroll = Scrollbar(main_frame)
main_scroll.pack(side=RIGHT, fill=Y)

main_scroll = Scrollbar(main_frame, orient='horizontal')
main_scroll.pack(side=BOTTOM, fill=X)

main_menu = ttk.Treeview(main_frame, yscrollcommand=main_scroll.set, xscrollcommand=main_scroll.set)

main_menu.pack()

main_scroll.config(command=main_menu.yview)
main_scroll.config(command=main_menu.xview)

# инициализация столбцов

main_menu['columns'] = ('udk', 'k_name', 'k_genre', 'manufacturer', 'release_year', 'out_date', 'out_time')

# формат столбцов
main_menu.column("#0", width=0, stretch=NO)
main_menu.column("udk", anchor=CENTER, width=110)
main_menu.column("k_name", anchor=CENTER, width=140)
main_menu.column("k_genre", anchor=CENTER, width=90)
main_menu.column("manufacturer", anchor=CENTER, width=120)
main_menu.column("release_year", anchor=CENTER, width=100)
main_menu.column("out_date", anchor=CENTER, width=100)
main_menu.column("out_time", anchor=CENTER, width=110)

# названия столбцов
main_menu.heading("#0", text="", anchor=CENTER)
main_menu.heading("udk", text=h1, anchor=CENTER)
main_menu.heading("k_name", text=h2, anchor=CENTER)
main_menu.heading("k_genre", text=h3, anchor=CENTER)
main_menu.heading("manufacturer", text=h4, anchor=CENTER)
main_menu.heading("release_year", text=h5, anchor=CENTER)
main_menu.heading("out_date", text=h6, anchor=CENTER)
main_menu.heading("out_time", text=h7, anchor=CENTER)

# считывает словарь в таблицу
for i in range(1, len(d)+1):
    main_menu.insert(parent='', index='end', iid=i - 1, text='', values=(
        d[str(i)]['udk'], d[str(i)]['k_name'], d[str(i)]['k_genre'], d[str(i)]['manufacturer'],
        d[str(i)]['release_year'],
        d[str(i)]['out_date'], d[str(i)]['out_time']))
main_menu.pack()

# добавление записей
Label(ws, text="Добавление записей", font=('Helvetica', 16, "bold")).pack()
Input_frame = Frame(ws)
Input_frame.pack()

# названия
toudk = Label(Input_frame, text=h1)
toudk.grid(row=0, column=0)

tok_name = Label(Input_frame, text=h2)
tok_name.grid(row=0, column=1)

tok_genre = Label(Input_frame, text=h3)
tok_genre.grid(row=0, column=2)

tomanufacturer = Label(Input_frame, text=h4)
tomanufacturer.grid(row=0, column=3)

torelease_year = Label(Input_frame, text=h5)
torelease_year.grid(row=0, column=4)

toout_date = Label(Input_frame, text=h6)
toout_date.grid(row=0, column=5)

toout_time = Label(Input_frame, text=h7)
toout_time.grid(row=0, column=6)

# столбцы
toudk = Entry(Input_frame)
toudk.grid(row=1, column=0)

tok_name = Entry(Input_frame)
tok_name.grid(row=1, column=1)

tok_genre = Entry(Input_frame)
tok_genre.grid(row=1, column=2)

tomanufacturer = Entry(Input_frame)
tomanufacturer.grid(row=1, column=3)

torelease_year = Entry(Input_frame)
torelease_year.grid(row=1, column=4)

toout_date = Entry(Input_frame)
toout_date.grid(row=1, column=5)

toout_time = Entry(Input_frame)
toout_time.grid(row=1, column=6)

# кнопка добавить
Input_button = Button(ws, text="Добавить", command=input_record)

Input_button.pack()

# удаление записей
Label(ws, text="Удаление записей", font=('Helvetica', 16, "bold")).pack()
Input_frame = Frame(ws)
Input_frame.pack()

udk = Label(Input_frame, text=h1)
udk.grid(row=0, column=0)

id_entry = Entry(Input_frame)
id_entry.grid(row=1, column=0)

# кнопка удалить
Remove_button = Button(ws, text="Удалить", command=input_record)

Remove_button.pack()

# кнопка основные функции
Label(ws, text="Другое", font=('Helvetica', 16, "bold")).pack()

Func_button = Button(ws, text="Открыть Основные функции", width=45, height=3, command=additional_menu)
Func_button.pack()

ws.mainloop()
