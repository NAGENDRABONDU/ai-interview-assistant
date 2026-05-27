from app.database.session_repository import (
    get_questions_db,
    get_answers_db,
    get_scores_db,
    get_feedback_db
)

sid = "7db0498b-0c01-4b39-ada1-9d98d03a3d0c"

print("Questions:", len(get_questions_db(sid)))
print("Answers:", len(get_answers_db(sid)))
print("Scores:", len(get_scores_db(sid)))
print("Feedback:", len(get_feedback_db(sid)))