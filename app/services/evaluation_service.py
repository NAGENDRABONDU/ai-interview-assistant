def evaluate_answer(answer: str):

    answer = answer.strip()

    if len(answer) < 10:
        return {
            "score": 2,
            "feedback": "Answer is too short."
        }

    elif len(answer) < 30:
        return {
            "score": 5,
            "feedback": "Good attempt. Add more explanation."
        }

    else:
        return {
            "score": 8,
            "feedback": "Good answer with reasonable explanation."
        }