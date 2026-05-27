from app.database.session_repository import add_question_db, get_questions_db

add_question_db(
    "test123",
    "What is Python?"
)

print(
    get_questions_db("test123")
)