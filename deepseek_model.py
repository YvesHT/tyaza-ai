import requests

API_KEY = "sk-8b3bcdd54d0d484697045990e4539c27"
API_URL = "https://api.deepseek.com/v1/chat/completions"

def get_answer(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "deepseek-chat",  # use correct model name
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
