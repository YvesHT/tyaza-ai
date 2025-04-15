from pydantic import BaseModel
import requests

API_KEY = "sk-..."  # keep your key

API_URL = "https://api.deepseek.com/v1/chat/completions"

def get_answer(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "deepseek-chat",
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
    except Exception:
        return "Sorry, I couldn’t reach my brain. Try again later."
