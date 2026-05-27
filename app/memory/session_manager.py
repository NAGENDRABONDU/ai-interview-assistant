from app.database.session_repository import (
    create_session_db_auto,
    get_session_db,
    add_question_db,
    add_answer_db,
    add_score_db,
    add_feedback_db,
    increment_question_db
)


def create_session(
    role,
    experience,
    interview_type
):

    return create_session_db_auto(
        role,
        experience,
        interview_type
    )


def get_session(session_id):

    session = get_session_db(
        session_id
    )

    if session is None:
        return None

    return dict(session)


def add_question(session_id, question):

    add_question_db(
        session_id,
        question
    )


def increment_question(session_id):

    increment_question_db(
        session_id
    )


def add_answer(session_id, answer):

    add_answer_db(
        session_id,
        answer
    )


def add_score(session_id, score):

    add_score_db(
        session_id,
        score
    )


def add_feedback(session_id, feedback):

    add_feedback_db(
        session_id,
        feedback
    )