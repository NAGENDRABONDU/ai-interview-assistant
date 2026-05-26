from app.database.session_repository import (
    create_session_db,
    get_session_db
)

create_session_db(
    "124",
    "Python Developer",
    "Fresher",
    "Technical",
    10
)

session = get_session_db("123")

print(dict(session))