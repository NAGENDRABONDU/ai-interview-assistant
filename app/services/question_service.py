from app.services.llm_service import ask_gemini

QUESTIONS = {
    "Python Developer": [
        "What is the difference between a List and Tuple in Python?",
        "Explain Python decorators.",
        "What are generators in Python?",
        "Explain exception handling in Python.",
        "What is inheritance in Python?",
        "What is polymorphism?",
        "What are Python modules?",
        "Explain lambda functions.",
        "What is multithreading in Python?",
        "What is the difference between deep copy and shallow copy?"
    ],

    "AI Engineer": [
        "What is Machine Learning?",
        "Difference between AI and Deep Learning?",
        "What is RAG?"
    ]
}


def generate_question(role, index=0):

    role_questions = QUESTIONS.get(role)

    if role_questions and index < len(role_questions):
        return role_questions[index]

    return (
        "Explain exception handling in Python."
    )

def generate_ai_question(
    role,
    experience,
    previous_questions
):

    prompt = f"""
You are an expert technical interviewer.

Role: {role}
Experience: {experience}

Questions already asked:
{previous_questions}

Generate ONE NEW interview question.

Rules:
- Do not repeat any previous question.
- Increase difficulty gradually.
- Ask only technical questions.
- Return only the question text.
"""

    response = ask_gemini(prompt)

    if response is None:
        return None

    return response.strip()