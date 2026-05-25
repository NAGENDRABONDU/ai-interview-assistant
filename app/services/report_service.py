def generate_report(session):

    total_score = sum(
        session["scores"]
    )

    total_questions = len(
        session["scores"]
    )

    average_score = (
        total_score / total_questions
        if total_questions > 0
        else 0
    )

    return {
        "totalQuestions": total_questions,
        "totalScore": total_score,
        "averageScore": round(
            average_score,
            2
        ),
        "strengths": [
            "Good communication",
            "Good technical understanding"
        ],
        "improvements": [
            "Add more detailed explanations"
        ]
    }