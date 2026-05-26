import sqlite3

conn = sqlite3.connect("test.db")

print("Connected Successfully")

conn.close()