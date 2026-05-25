from fastapi import FastAPI

from app.routes.interview import router as interview_router

app = FastAPI(
    title="AI Interview Assistant"
)


@app.get("/")
def home():
    return {
        "message": "AI Interview Assistant API"
    }


@app.get("/health")
def health():
    return {
        "success": True,
        "status": "healthy"
    }


app.include_router(
    interview_router,
    prefix="/api/interview",
    tags=["Interview"]
)