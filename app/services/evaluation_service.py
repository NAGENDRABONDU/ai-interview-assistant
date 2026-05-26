from app.services.llm_service import ask_gemini
import json
import re


def evaluate_answer(question, answer):

    prompt = f"""
You are a technical interviewer.

Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer.

Return ONLY valid JSON.

Example:

{{
    "score": 8,
    "feedback": "Good answer."
}}
"""

    response = ask_gemini(prompt)
    if response is None:
        return {
            "score": 5,
            "feedback": "AI evaluation temporarily unavailable. Using fallback evaluation."
    }

    try:
        # Remove markdown code fences
        cleaned = re.sub(
            r"```json|```",
            "",
            response
        ).strip()

        result = json.loads(cleaned)

        return {
            "score": int(result["score"]),
            "feedback": result["feedback"]
        }

    except Exception as e:

        return {
            "score": 5,
            "feedback": f"JSON Parse Error: {str(e)}"
        }