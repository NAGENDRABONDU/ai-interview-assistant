# test_start.py

from app.memory.session_manager import create_session, add_question
from app.database.session_repository import get_questions_db

sid = create_session(
    "Python Developer",
    "Fresher",
    "Technical"
)

add_question(
    sid,
    "Test Question"
)

print(
    get_questions_db(sid)
)