import uuid
from app.database.db import get_connection


def create_session_db(
    session_id,
    role,
    experience,
    interview_type,
    max_questions
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO sessions (
            session_id,
            role,
            experience,
            interview_type,
            current_question,
            max_questions
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            session_id,
            role,
            experience,
            interview_type,
            0,
            max_questions
        )
    )

    conn.commit()
    conn.close()

def get_session_db(session_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM sessions
        WHERE session_id = ?
        """,
        (session_id,)
    )

    row = cursor.fetchone()

    conn.close()

    return row
def create_session_db_auto(
    role,
    experience,
    interview_type,
    max_questions=10
):

    session_id = str(uuid.uuid4())

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO sessions (
            session_id,
            role,
            experience,
            interview_type,
            current_question,
            max_questions
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            session_id,
            role,
            experience,
            interview_type,
            0,
            max_questions
        )
    )

    conn.commit()
    conn.close()

    return session_id