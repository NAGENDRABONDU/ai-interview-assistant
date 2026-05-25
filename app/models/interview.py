from pydantic import BaseModel, Field


class StartInterviewRequest(BaseModel):
    role: str = Field(..., min_length=2)
    experience: str = Field(..., min_length=2)
    interviewType: str = Field(..., min_length=2)

class AnswerRequest(BaseModel):
    sessionId: str
    answer: str