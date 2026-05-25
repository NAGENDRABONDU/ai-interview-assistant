from fastapi import APIRouter, HTTPException

from app.models.interview import (
    StartInterviewRequest,
    AnswerRequest
)
from app.memory.session_manager import (
    create_session,
    add_question,
    add_answer,
    add_score,
    add_feedback,
    get_session,
    increment_question
)
from app.services.question_service import generate_question
from app.services.evaluation_service import evaluate_answer
from app.services.report_service import generate_report
from app.utils.logger import logger

router = APIRouter()


@router.post("/start")
def start_interview(data: StartInterviewRequest):

    session_id = create_session(
        role=data.role,
        experience=data.experience,
        interview_type=data.interviewType
    )

    logger.info(f"Session Created : {session_id}")

    question = generate_question(data.role)

    add_question(session_id, question)

    return {
     "success": True,
     "sessionId": session_id,
     "question": question
   }


@router.get("/session/{session_id}")
def session_details(session_id: str):

    session = get_session(session_id)

    if session is None:
        raise HTTPException(
            status_code=404,
            detail="Session not found"
        )

    return {
        "success": True,
        "data": session
    }


@router.post("/answer")
def submit_answer(data: AnswerRequest):

    add_answer(
        data.sessionId,
        data.answer
    )

    result = evaluate_answer(
        data.answer
    )

    add_score(
        data.sessionId,
        result["score"]
    )

    add_feedback(
        data.sessionId,
        result["feedback"]
    )

    increment_question(data.sessionId)

    session = get_session(data.sessionId)

    next_question = generate_question(
        session["role"],
        session["current_question"]
    )

    if next_question is None:

        report = generate_report(
            session
        )

        return {
            "success": True,
            "interviewCompleted": True,
            "report": report
        }

    if next_question:
        add_question(
            data.sessionId,
            next_question
        )

    return {
        "success": True,
        "score": result["score"],
        "feedback": result["feedback"],
        "nextQuestion": next_question
    }