from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

# FastAPI initialization
app = FastAPI()

# Define API key and URL for DeepSeek API
API_KEY = "sk-8b3bcdd54d0d484697045990e4539c27"
API_URL = "https://api.deepseek.com/v1/chat/completions"

# Create a Pydantic model for the incoming request
class QuestionRequest(BaseModel):
    question: str

# Function to get answer from DeepSeek API
def get_answer(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "deepseek-chat",  # Use correct model name
        "messages": [
            {"role": "system", "content": "You are Tyaza, a helpful mental health assistant who speaks Kinyarwanda."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        return "Sorry, I couldn’t reach my brain. Try again later."

@app.post('/ask')
async def ask_tyaza(data: QuestionRequest):
    question = data.question
    if not question:
        raise HTTPException(status_code=400, detail="Please ask something.")
    answer = get_answer(question)
    return {"answer": answer}

# Run the app using 'uvicorn' (instead of Flask's built-in server)
