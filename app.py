from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from deepseek_model import get_answer
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI()

# Allow frontend to access this backend (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this for specific allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Create a Pydantic model for the incoming request
class QuestionRequest(BaseModel):
    question: str

@app.post('/ask')
async def ask_tyaza(data: QuestionRequest):
    question = data.question
    if not question:
        raise HTTPException(status_code=400, detail="Please ask something.")
    answer = get_answer(question)
    return {"answer": answer}

# Run the app using 'uvicorn' (instead of Flask's built-in server)
