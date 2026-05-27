from app.database.session_repository import get_questions_db

questions = get_questions_db("123")

print(questions)