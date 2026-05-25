import uuid

sessions = {}


def create_session(role, experience, interview_type):
    session_id = str(uuid.uuid4())

    sessions[session_id] = {
        "role": role,
        "experience": experience,
        "interview_type": interview_type,
        "current_question": 0,
        "questions": [],
        "answers": [],
        "scores": [],
        "feedback": []
    }
    # print(sessions)
    return session_id


def get_session(session_id):
    return sessions.get(session_id)

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
