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
from app.services.question_service import (
    generate_question,
    generate_ai_question
)
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

    question = generate_ai_question(
        data.role,
        data.experience,
        []
    )

    if not question:
        question = generate_question(
            data.role,
            0
        )

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

    # Get session
    session = get_session(data.sessionId)

    if session is None:
        raise HTTPException(
            status_code=404,
            detail="Session not found"
        )

    # Check interview completion
    if session["current_question"] >= session["max_questions"]:
        report = generate_report(session)

        return {
            "success": True,
            "interviewCompleted": True,
            "report": report
        }

    # Store answer
    add_answer(
        data.sessionId,
        data.answer
    )

    # Current question
    current_question = session["questions"][-1]

    # Evaluate answer
    result = evaluate_answer(
        current_question,
        data.answer
    )

    # Store evaluation
    add_score(
        data.sessionId,
        result["score"]
    )

    add_feedback(
        data.sessionId,
        result["feedback"]
    )

    # Increment question counter
    increment_question(data.sessionId)

    # Reload updated session
    session = get_session(data.sessionId)

    # Interview completed?
    if session["current_question"] >= session["max_questions"]:

        report = generate_report(session)

        return {
            "success": True,
            "interviewCompleted": True,
            "report": report
        }

    # Generate next question
    try:
        next_question = generate_ai_question(
            session["role"],
            session["experience"],
            session["questions"]
        )

        if not next_question:
            next_question = generate_question(
                session["role"],
                session["current_question"]
            )

    except Exception:

        next_question = generate_question(
            session["role"],
            session["current_question"]
        )

    # Safety check
    if next_question is None:

        report = generate_report(session)

        return {
            "success": True,
            "interviewCompleted": True,
            "report": report
        }

    # Store next question
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

    # Get session
    session = get_session(data.sessionId)
    if session is None:
        raise HTTPException(
            status_code=404,
            detail="Session not found"
    )
    if session["current_question"] >= session["max_questions"]:

        report = generate_report(session)

        return {
            "success": True,
            "interviewCompleted": True,
            "report": report
    }

    if session is None:
        raise HTTPException(
            status_code=404,
            detail="Session not found"
        )

    # Store candidate answer
    add_answer(
        data.sessionId,
        data.answer
    )

    # Get current question for evaluation
    current_question = session["questions"][-1]

    # Gemini evaluation
    result = evaluate_answer(
        current_question,
        data.answer
    )

    # Store score and feedback
    add_score(
        data.sessionId,
        result["score"]
    )

    add_feedback(
        data.sessionId,
        result["feedback"]
    )

    # Move to next question
    increment_question(data.sessionId)

    # Reload updated session
    session = get_session(data.sessionId)

    # Generate next question
    try:
        next_question = generate_ai_question(
            session["role"],
            session["experience"],
            session["questions"]
        )
        if not next_question:
            next_question = generate_question(
                session["role"],
                session["current_question"]
            )
    except Exception:
        next_question = generate_question(
            session["role"],
            session["current_question"]
        )
    
    # Store next question
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