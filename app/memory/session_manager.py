import uuid

from app.database.session_repository import (
    create_session_db_auto,
    get_session_db
)
sessions = {}


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

def update_session(session_id, key, value):
    if session_id in sessions:
        sessions[session_id][key] = value

def add_question(session_id, question):

    if session_id in sessions:
        sessions[session_id]["questions"].append(question)

def increment_question(session_id):

    if session_id in sessions:
        sessions[session_id]["current_question"] += 1

def add_answer(session_id, answer):

    if session_id in sessions:
        sessions[session_id]["answers"].append(answer)

def add_score(session_id, score):

    if session_id in sessions:
        sessions[session_id]["scores"].append(score)

def add_feedback(session_id, feedback):

    if session_id in sessions:
        sessions[session_id]["feedback"].append(feedback)
