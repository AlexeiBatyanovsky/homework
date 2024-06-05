import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

def execu():
    

with connection:
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    login TEXT NOT NULL,
    password TEXT NOT NULL,
    blocked TEXT NOT NULL,
    subscription_mode TEXT NOT NULL,
    subscription_date TEXT NOT NULL)
    ''')

with connection:
    cursor.execute('''
                    INSERT INTO Users (name, login, password, blocked, subscription_mode, subscription_date) 
                    VALUES (?, ?, ?, ? ,?, ?)''',
                    ('Вася', 'djhcvjsh', 'djhc35Dvjsh', 'false', '', ''))