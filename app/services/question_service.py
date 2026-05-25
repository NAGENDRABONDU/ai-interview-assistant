QUESTIONS = {
    "Python Developer": [
        "What is the difference between a List and Tuple in Python?",
        "Explain Python decorators.",
        "What are generators in Python?"
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

    return None

