from app.database.session_repository import get_scores_db


def generate_report(session):

    scores = get_scores_db(
        session["session_id"]
    )

    total_score = sum(scores)

    total_questions = len(scores)

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