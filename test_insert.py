from app.database.session_repository import add_question_db

add_question_db(
    "123",
    "What is Python?"
)

print("Question Inserted")