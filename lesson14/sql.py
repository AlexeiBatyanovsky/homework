"""
Используя класс из пред.урока обеспечить хранение и сохранение любых изменений в базе 
данных. Для этого можно к примеру добавить в класс метод save который будет сохранять или 
создавать пользователя в базе данных и использовать его при любых изменениях.


* в базе данных создать таблицу предоставляемых услуг со след полями
	название
	тип (1 - платная 0 - бесплатная)
	стоимость 
	период в днях
** в класс пользователя добавить методы:
	добавить услугу (услуг у одного пользователя может быть несколько)
	продлить услугу (продлить можно если услуга еще не закончена, иначе добавить)
	удалить услугу
*** создать консольное или оконное приложение которое показывает меню и отрабатывает выбранный пункт.
	Меню:
		1 - показать пользователей
		2 - информация о пользователе (в т.ч. и подключенные услуги)
		3 - список услуг		
		4 - показать пользователей с определенной услугой
		5 - показать пользователей у которых за прошедший месяц окончился период хоть одной услуги 
 
	
 
"""


import sqlite3
# from sqlite3 import Error
from tkinter import *
from tkinter import messagebox
from User import User

# def create_connection(path):
    
#     connection = None
#     try:
#         connection = sqlite3.connect(path)
#         print("Connection to SQLite DB successful")
#     except Error as e:
#         print(f"The error '{e}' occurred")

#     return connection

# def execute_query(connection, query):
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         connection.commit()
#         print("Query executed successfully")
#     except Error as e:
#         print(f"The error '{e}' occurred")

# def execute_read_query(connection, query):
#     cursor = connection.cursor()
#     result = None
#     try:
#         cursor.execute(query)
#         result = cursor.fetchall()
#         return result
#     except Error as e:
#         print(f"The error '{e}' occurred")

def button1():  
    messagebox.showinfo('Пользователи', result)
def button2():  
    messagebox.showinfo('Информация о пользователе')
def button3():
    messagebox.showinfo('Доступные услуги', services)
def button4():  
    messagebox.showinfo('Пользователи с определенной услугой')
def button5():  
    messagebox.showinfo('Пользователи у которых за прошедший месяц окончился период хоть одной услуги ')
    
connection = sqlite3.connect('base.db')
cur = connection.cursor()

Table1 ='''
            CREATE TABLE IF NOT EXISTS Services (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            type INTEGER,
            price INTEGER,
            duration INTEGER)
        '''
cur.execute(Table1)

with connection:
    services = [('sport', 0, 0, 30),
               ('music', 1, 200, 60),
               ('movie', 1, 250, 30),
               ('relax', 1, 150, 90)]
    
    cur.executemany("INSERT INTO Services VALUES(?,?,?,?)",services)

Table2 ='''
            CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            login TEXT NOT NULL,
            password TEXT NOT NULL)
        '''
cur.execute(Table2)
with connection:
    users = [('Viktor', 'Vic', 'A5ffds'),
            ('Anton', 'Antony', 'ds54Ertsf'),
            ('Alexei', 'Alex', 'sfS56sd'),
            ('Dmitrii', 'dimon', 'sa4Dvf9')]
    cur.executemany("INSERT INTO Users VALUES(?,?,?,?)",users)

select_users = "SELECT * from users"
users1 = cur.execute(select_users)
result = cur.fetchall()

win = Tk()
win.geometry('550x200')
win.title('Menu')
    
btn = Button(win, text='Показать пользователей', command=button1)  
btn.grid(column=0, row=0)  
btn2 = Button(win, text="Информация о пользователе",command=button2)  
btn2.grid(column=0, row=1)  
btn3 = Button(text='Cписок услуг', command=button3)
btn3.grid(column=0, row=2)
btn4 = Button(text='Показать пользователей с определенной услугой', command=button4)
btn4.grid(column=0, row=3)
btn5 = Button(text='Показать пользователей у которых за прошедший месяц окончился период хоть одной услуги ', command=button5)
btn5.grid(column=0, row=4)



win.mainloop()