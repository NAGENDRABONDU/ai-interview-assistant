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


def increment_question_db(session_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE sessions
        SET current_question = current_question + 1
        WHERE session_id = ?
        """,
        (session_id,)
    )

    conn.commit()
    conn.close()


def add_question_db(session_id, question):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO questions (
            session_id,
            question
        )
        VALUES (?, ?)
        """,
        (session_id, question)
    )

    conn.commit()
    conn.close()


def add_answer_db(session_id, answer):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO answers (
            session_id,
            answer
        )
        VALUES (?, ?)
        """,
        (session_id, answer)
    )

    conn.commit()
    conn.close()


def add_score_db(session_id, score):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO scores (
            session_id,
            score
        )
        VALUES (?, ?)
        """,
        (session_id, score)
    )

    conn.commit()
    conn.close()


def add_feedback_db(session_id, feedback):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO feedback (
            session_id,
            feedback
        )
        VALUES (?, ?)
        """,
        (session_id, feedback)
    )

    conn.commit()
    conn.close()


def get_questions_db(session_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT question
        FROM questions
        WHERE session_id = ?
        ORDER BY id
        """,
        (session_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    return [row["question"] for row in rows]


def get_answers_db(session_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT answer
        FROM answers
        WHERE session_id = ?
        ORDER BY id
        """,
        (session_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    return [row["answer"] for row in rows]


def get_scores_db(session_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT score
        FROM scores
        WHERE session_id = ?
        ORDER BY id
        """,
        (session_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    return [row["score"] for row in rows]


def get_feedback_db(session_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT feedback
        FROM feedback
        WHERE session_id = ?
        ORDER BY id
        """,
        (session_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    return [row["feedback"] for row in rows]


def get_all_sessions():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM sessions
        ORDER BY rowid DESC
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]