from app.database.session_repository import (
    get_session_db,
    increment_question_db
)

sid = "7db0498b-0c01-4b39-ada1-9d98d03a3d0c"

print("Before:")
print(dict(get_session_db(sid)))

increment_question_db(sid)

print("After:")
print(dict(get_session_db(sid)))