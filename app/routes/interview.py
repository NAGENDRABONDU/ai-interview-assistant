from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from app.services.pdf_service import (
    generate_pdf_report
)
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

from app.database.session_repository import (
    get_questions_db,
    get_answers_db,
    get_scores_db,
    get_feedback_db,
    get_all_sessions
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

    add_question(
        session_id,
        question
    )

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


@router.get("/history")
def interview_history():

    sessions = get_all_sessions()

    return {
        "success": True,
        "count": len(sessions),
        "data": sessions
    }


@router.get("/history/{session_id}")
def interview_details(session_id: str):

    session = get_session(session_id)

    if session is None:
        raise HTTPException(
            status_code=404,
            detail="Session not found"
        )

    questions = get_questions_db(session_id)
    answers = get_answers_db(session_id)
    scores = get_scores_db(session_id)
    feedback = get_feedback_db(session_id)

    interview_data = []

    for i in range(len(questions)):

        interview_data.append({
            "question": questions[i],
            "answer": answers[i] if i < len(answers) else None,
            "score": scores[i] if i < len(scores) else None,
            "feedback": feedback[i] if i < len(feedback) else None
        })

    return {
        "success": True,
        "session": session,
        "interview": interview_data
    }


@router.post("/answer")
def submit_answer(data: AnswerRequest):

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

    add_answer(
        data.sessionId,
        data.answer
    )

    questions = get_questions_db(
        data.sessionId
    )

    current_question = questions[-1]

    result = evaluate_answer(
        current_question,
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

    increment_question(
        data.sessionId
    )

    session = get_session(
        data.sessionId
    )

    if session["current_question"] >= session["max_questions"]:

        report = generate_report(session)

        return {
            "success": True,
            "interviewCompleted": True,
            "report": report
        }

    try:

        next_question = generate_ai_question(
            session["role"],
            session["experience"],
            questions
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

    if next_question is None:

        report = generate_report(session)

        return {
            "success": True,
            "interviewCompleted": True,
            "report": report
        }

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


@router.get("/report/{session_id}")
def interview_report(session_id: str):

    session = get_session(session_id)

    if session is None:
        raise HTTPException(
            status_code=404,
            detail="Session not found"
        )

    report = generate_report(session)

    return {
        "success": True,
        "report": report
    }


@router.get("/report/{session_id}/pdf")
def download_pdf_report(session_id: str):

    session = get_session(
        session_id
    )

    if session is None:
        raise HTTPException(
            status_code=404,
            detail="Session not found"
        )

    report = generate_report(
        session
    )

    pdf_file = (
        f"report_{session_id}.pdf"
    )

    generate_pdf_report(
        session,
        report,
        pdf_file
    )

    return FileResponse(
        pdf_file,
        media_type="application/pdf",
        filename=pdf_file
    )