from app.services.llm_service import ask_gemini

response = ask_gemini(
    "Explain Python in one sentence."
)

print(response)