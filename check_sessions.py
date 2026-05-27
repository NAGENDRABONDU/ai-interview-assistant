import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute(
    """
    SELECT session_id,
           current_question,
           max_questions
    FROM sessions
    """
)

for row in cursor.fetchall():
    print(row)

conn.close()