import sqlite3

db_name = 'database.db'
connection = None
cursor = None

def open():
    global connection, cursor
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor

def create():
    open()
    cursor.execute()
  