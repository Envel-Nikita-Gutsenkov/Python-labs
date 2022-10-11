from tkinter import *
from tkinter import ttk

d = {}

h1 = "УДК  кассеты"
h2 = "Название фильма"
h3 = "Жанр"
h4 = "Производитель"
h5 = "Год выпуска"
h6 = "Дата проката"
h7 = "Время проката"

ws = Tk()
ws.title('Лабораторная работа 7')
ws.geometry('1300x600')

Label(ws, text="Список записей", font=('Helvetica', 16, "bold")).pack()

game_frame = Frame(ws)
game_frame.pack()

# scrollbar
game_scroll = Scrollbar(game_frame)
game_scroll.pack(side=RIGHT, fill=Y)

game_scroll = Scrollbar(game_frame, orient='horizontal')
game_scroll.pack(side=BOTTOM, fill=X)

my_game = ttk.Treeview(game_frame, yscrollcommand=game_scroll.set, xscrollcommand=game_scroll.set)

my_game.pack()

game_scroll.config(command=my_game.yview)
game_scroll.config(command=my_game.xview)

# define our column

my_game['columns'] = ('udk', 'k_name', 'k_genre', 'manufacturer', 'release_year', 'out_date', 'out_time')

# format our column
my_game.column("#0", width=0, stretch=NO)
my_game.column("udk", anchor=CENTER, width=110)
my_game.column("k_name", anchor=CENTER, width=140)
my_game.column("k_genre", anchor=CENTER, width=90)
my_game.column("manufacturer", anchor=CENTER, width=120)
my_game.column("release_year", anchor=CENTER, width=100)
my_game.column("out_date", anchor=CENTER, width=100)
my_game.column("out_time", anchor=CENTER, width=110)

# Create Headings
my_game.heading("#0", text="", anchor=CENTER)
my_game.heading("udk", text=h1, anchor=CENTER)
my_game.heading("k_name", text=h2, anchor=CENTER)
my_game.heading("k_genre", text=h3, anchor=CENTER)
my_game.heading("manufacturer", text=h4, anchor=CENTER)
my_game.heading("release_year", text=h5, anchor=CENTER)
my_game.heading("out_date", text=h6, anchor=CENTER)
my_game.heading("out_time", text=h7, anchor=CENTER)

# add data
my_game.insert(parent='', index='end', iid=0, text='',
               values=('1', 'Ninja', '101', 'Oklahoma', 'Moore'))
my_game.insert(parent='', index='end', iid=1, text='',
               values=('2', 'Ranger', '102', 'Wisconsin', 'Green Bay'))
my_game.insert(parent='', index='end', iid=2, text='',
               values=('3', 'Deamon', '103', 'California', 'Placentia'))
my_game.insert(parent='', index='end', iid=3, text='',
               values=('4', 'Dragon', '104', 'New York', 'White Plains'))
my_game.insert(parent='', index='end', iid=4, text='',
               values=('5', 'CrissCross', '105', 'California', 'San Diego'))
my_game.insert(parent='', index='end', iid=5, text='',
               values=('6', 'ZaqueriBlack', '106', 'Wisconsin', 'TONY'))
my_game.insert(parent='', index='end', iid=6, text='',
               values=('7', 'RayRizzo', '107', 'Colorado', 'Denver'))
my_game.insert(parent='', index='end', iid=7, text='',
               values=('8', 'Byun', '108', 'Pennsylvania', 'ORVISTON'))
my_game.insert(parent='', index='end', iid=8, text='',
               values=('9', 'Trink', '109', 'Ohio', 'Cleveland'))
my_game.insert(parent='', index='end', iid=9, text='',
               values=('10', 'Twitch', '110', 'Georgia', 'Duluth'))
my_game.insert(parent='', index='end', iid=10, text='',
               values=('11', 'Animus', '111', 'Connecticut', 'Hartford'))
my_game.pack()

# добавление записей
Label(ws, text="Добавление записей", font=('Helvetica', 16, "bold")).pack()
Input_frame = Frame(ws)
Input_frame.pack()

udk = Label(Input_frame, text=h1)
udk.grid(row=0, column=0)

k_name = Label(Input_frame, text=h2)
k_name.grid(row=0, column=1)

k_genre = Label(Input_frame, text=h3)
k_genre.grid(row=0, column=2)

manufacturer = Label(Input_frame, text=h4)
manufacturer.grid(row=0, column=3)

release_year = Label(Input_frame, text=h5)
release_year.grid(row=0, column=4)

out_date = Label(Input_frame, text=h6)
out_date.grid(row=0, column=5)

out_time = Label(Input_frame, text=h7)
out_time.grid(row=0, column=6)

id_entry = Entry(Input_frame)
id_entry.grid(row=1, column=0)

fullname_entry = Entry(Input_frame)
fullname_entry.grid(row=1, column=1)

award_entry = Entry(Input_frame)
award_entry.grid(row=1, column=2)

award_entry = Entry(Input_frame)
award_entry.grid(row=1, column=3)

award_entry = Entry(Input_frame)
award_entry.grid(row=1, column=4)

award_entry = Entry(Input_frame)
award_entry.grid(row=1, column=5)

award_entry = Entry(Input_frame)
award_entry.grid(row=1, column=6)

def input_record():
    global count

    set.insert(parent='', index='end', iid=count, text='',
               values=(udk.get(), k_name.get(), k_genre.get()))
    count += 1

    udk.delete(0, END)
    k_name.delete(0, END)
    k_genre.delete(0, END)


# button
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

def remove_record():
    global count

    set.insert(parent='', index='end', iid=count, text='',
               values=(udk.get(), k_name.get(), k_genre.get()))
    count += 1

    udk.delete(0, END)
    k_name.delete(0, END)
    k_genre.delete(0, END)


# button
Remove_button = Button(ws, text="Удалить", command=input_record)

Remove_button.pack()

Label(ws, text="Другое", font=('Helvetica', 16, "bold")).pack()

Func_button = Button(ws, text="Открыть Основные функции", width=45, height=3, command=input_record)
Func_button.pack()

def quit():
    print("Have a great day! Goodbye :)")
    sys.exit(0)


ws.mainloop()
