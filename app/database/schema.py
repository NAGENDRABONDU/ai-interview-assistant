from app.database.db import get_connection


def create_tables():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sessions (
        session_id TEXT PRIMARY KEY,
        role TEXT,
        experience TEXT,
        interview_type TEXT,
        current_question INTEGER,
        max_questions INTEGER
    )
    """)

    conn.commit()
    conn.close()

    print("Tables Created")