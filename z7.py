from tkinter import *
from tkinter import ttk

d = {
    "id": ["0", "1", "2"],
    "udk": ["1.22", "2.66", "3.44"],
    "k_name": ["Name1", "Name2", "Name3"],
    "k_genre": ["Genre1", "Genre1", "Genre1"],
    "manufacturer": ["Manuf1", "Manuf2", "Manuf3"],
    "release_year": [2000, 2000, 2000],
    "out_date": ["01.01", "01.01", "01.01"],
    "out_time": ["10.02", "10.02", "10.02"]
}

# предустановленное количество строк (от 0)
count = 3

h0 = "ID"
h1 = "УДК  кассеты"
h2 = "Название фильма"
h3 = "Жанр"
h4 = "Производитель"
h5 = "Год выпуска"
h6 = "Дата проката"
h7 = "Время проката"


# ЛОГИКА

# удаление записи
def remove_record():
    toremove = d['id'].index(id_entry.get())

    d['id'].pop(toremove)
    d['udk'].pop(toremove)
    d['k_name'].pop(toremove)
    d['k_genre'].pop(toremove)
    d['manufacturer'].pop(toremove)
    d['release_year'].pop(toremove)
    d['out_date'].pop(toremove)
    d['out_time'].pop(toremove)

    delete_entries()

    tableupdate()

# добавление записи
def input_record():
    global count
    count += 1

    d['id'].append(str(count))
    d['udk'].append(toudk.get())
    d['k_name'].append(tok_name.get())
    d['k_genre'].append(tok_genre.get())
    d['manufacturer'].append(tomanufacturer.get())
    d['release_year'].append(torelease_year.get())
    d['out_date'].append(toout_date.get())
    d['out_time'].append(toout_time.get())

    delete_entries()

    tableupdate()

# считывает словарь в таблицу
def tableupdate():
    main_menu.delete(*main_menu.get_children())

    for i in range(0, len(d['id'])):
        main_menu.insert(parent='', index='end', text='', values=(
            d['id'][i], d['udk'][i], d['k_name'][i], d['k_genre'][i], d['manufacturer'][i], d['release_year'][i],
            d['out_date'][i],
            d['out_time'][i]))

    main_menu.pack()

# удаление по году выпуска
def yearremove(year):
    indx = search(d['release_year'], year)
    # список для удаления нужен в порядке убывания индексов
    indx.reverse()

    for i in indx:
        print(i)
        d['id'].pop(i)
        d['udk'].pop(i)
        d['k_name'].pop(i)
        d['k_genre'].pop(i)
        d['manufacturer'].pop(i)
        d['release_year'].pop(i)
        d['out_date'].pop(i)
        d['out_time'].pop(i)

    tableupdate()

# заменить udk
def replaceudk(name, to):
    indx = search(d['k_name'], name)
    d['udk'][indx[0]] = to

    tableupdate()

# все фильмы заданного производителя
def searchfilms(name):
    indx = search(d['manufacturer'], name)
    main_menu.delete(*main_menu.get_children())

    for i in indx:
        main_menu.insert(parent='', index='end', text='', values=(
            d['id'][i], d['udk'][i], d['k_name'][i], d['k_genre'][i], d['manufacturer'][i], d['release_year'][i],
            d['out_date'][i],
            d['out_time'][i]))

    main_menu.pack()

# находит список интексов, содержащих запрошенное значение
def search(list, item):
    indx = []
    for idx, value in enumerate(list):
        if str(value) == str(item):
            indx.append(idx)
    return indx

# очищает поля ввода
def delete_entries():
  for field in fields:
    field.delete(0, END)

# ИНТЕРФЕЙС

# основные функции
def additional_menu():
    ws2 = Tk()
    ws2.title('Лабораторная работа 7 - Основные функции')
    ws2.geometry('600x400')

    # удаление записей по году выпуска
    Label(ws2, text="Удаление всех записей с заданным", font=('Helvetica', 16, "bold")).pack()
    Input_frame = Frame(ws2)
    Input_frame.pack()

    # название
    amrelease_year = Label(Input_frame, text=h5)
    amrelease_year.grid(row=0, column=0)

    # столбец
    amrelease_year = Entry(Input_frame)
    amrelease_year.grid(row=1, column=0)

    Button(ws2, text="Удалить", command=lambda: (yearremove(amrelease_year.get()), ws2.destroy())).pack()

    # заменить удк кассеты
    Label(ws2, text="Заменить УДК кассеты", font=('Helvetica', 16, "bold")).pack()
    Input_frame = Frame(ws2)
    Input_frame.pack()

    # названия
    amk_name = Label(Input_frame, text=h2)
    amk_name.grid(row=0, column=0)
    amudk_to = Label(Input_frame, text="Заменить УДК на")
    amudk_to.grid(row=0, column=1)

    # столбцы
    amk_name = Entry(Input_frame)
    amk_name.grid(row=1, column=0)
    amudk_to = Entry(Input_frame)
    amudk_to.grid(row=1, column=1)

    # кнопка добавить
    Button(ws2, text="Применить", command=lambda: (replaceudk(amk_name.get(), amudk_to.get()), ws2.destroy())).pack()

    Input_button.pack()

    # все сведения по производителю
    Label(ws2, text="Все сведения о фильмах заданного", font=('Helvetica', 16, "bold")).pack()
    Input_frame = Frame(ws2)
    Input_frame.pack()

    ammanufacturer = Label(Input_frame, text=h4)
    ammanufacturer.grid(row=0, column=0)

    # столбец
    ammanufacturer = Entry(Input_frame)
    ammanufacturer.grid(row=1, column=0)

    Button(ws2, text="Показать", command=lambda: (searchfilms(ammanufacturer.get()))).pack()
    Button(ws2, text="Отмена", command=lambda: (tableupdate(), ws2.destroy())).pack()

    ws2.mainloop()

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

main_menu['columns'] = ('id', 'udk', 'k_name', 'k_genre', 'manufacturer', 'release_year', 'out_date', 'out_time')

# формат столбцов
main_menu.column("#0", width=0, stretch=NO)
main_menu.column("id", anchor=CENTER, width=35)
main_menu.column("udk", anchor=CENTER, width=110)
main_menu.column("k_name", anchor=CENTER, width=150)
main_menu.column("k_genre", anchor=CENTER, width=90)
main_menu.column("manufacturer", anchor=CENTER, width=130)
main_menu.column("release_year", anchor=CENTER, width=110)
main_menu.column("out_date", anchor=CENTER, width=110)
main_menu.column("out_time", anchor=CENTER, width=120)

# названия столбцов
main_menu.heading("#0", text="", anchor=CENTER)
main_menu.heading("id", text=h0, anchor=CENTER)
main_menu.heading("udk", text=h1, anchor=CENTER)
main_menu.heading("k_name", text=h2, anchor=CENTER)
main_menu.heading("k_genre", text=h3, anchor=CENTER)
main_menu.heading("manufacturer", text=h4, anchor=CENTER)
main_menu.heading("release_year", text=h5, anchor=CENTER)
main_menu.heading("out_date", text=h6, anchor=CENTER)
main_menu.heading("out_time", text=h7, anchor=CENTER)

tableupdate()

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

id = Label(Input_frame, text=h0)
id.grid(row=0, column=0)

id_entry = Entry(Input_frame)
id_entry.grid(row=1, column=0)

# кнопка удалить
Remove_button = Button(ws, text="Удалить", command=remove_record)

Remove_button.pack()

# кнопка основные функции
Label(ws, text="Другое", font=('Helvetica', 16, "bold")).pack()

Func_button = Button(ws, text="Открыть Основные функции", width=45, height=3, command=additional_menu)
Func_button.pack()

# список полей для очистки
fields = toout_time, toout_date, torelease_year, tomanufacturer, tok_genre, tok_name, toudk, id_entry

# стиль
style = ttk.Style()
style.theme_use('clam')

ws.mainloop()
