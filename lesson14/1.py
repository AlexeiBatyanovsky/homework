import sqlite3
# from sqlite3 import Error
from tkinter import *
from tkinter import messagebox
from User import User

connection = sqlite3.connect('base.db')
cursor = connection.cursor()

users1 =[
      User('Василий','Vasilii'),
      User('Анатолий', 'Anatolii'),
      User('Александр', 'Aleksandr')
]

with connection:
    cursor.executemany("INSERT INTO users1 VALUES(?,?,?,?,?,?)",users1)