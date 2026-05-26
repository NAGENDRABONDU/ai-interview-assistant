from app.services.question_service import generate_ai_question

question = generate_ai_question(
    role="Python Developer",
    experience="Fresher",
    previous_questions=[]
)

print(question)