import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM sessions")
cursor.execute("DELETE FROM questions")
cursor.execute("DELETE FROM answers")
cursor.execute("DELETE FROM scores")
cursor.execute("DELETE FROM feedback")

conn.commit()
conn.close()

print("Database Reset")