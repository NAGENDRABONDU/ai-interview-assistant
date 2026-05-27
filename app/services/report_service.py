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

    highest_score = (
        max(scores)
        if scores
        else 0
    )

    lowest_score = (
        min(scores)
        if scores
        else 0
    )

    if average_score >= 8:
        performance = "Excellent"

    elif average_score >= 6:
        performance = "Good"

    elif average_score >= 4:
        performance = "Average"

    else:
        performance = "Needs Improvement"

    if average_score >= 8:
    
        strengths = [
            "Strong Python fundamentals",
            "Good problem solving"
        ]
    
        improvements = [
            "Explore advanced topics"
        ]
    
    elif average_score >= 5:
    
        strengths = [
            "Basic concepts understood"
        ]
    
        improvements = [
            "Provide more detailed explanations",
            "Improve coding examples"
        ]
    
    else:
    
        strengths = [
            "Attempted all questions"
        ]
    
        improvements = [
            "Revise Python fundamentals",
            "Practice coding exercises",
            "Improve interview communication"
        ]
    
    
    return {
        "totalQuestions": total_questions,
        "totalScore": total_score,
        "averageScore": round(
            average_score,
            2
        ),
        "highestScore": highest_score,
        "lowestScore": lowest_score,
        "performance": performance,
        "strengths": strengths,
        "improvements": improvements
    }