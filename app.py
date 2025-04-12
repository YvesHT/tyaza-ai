from flask import Flask, request, jsonify
from deepseek_model import get_answer
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to access this backend

@app.route('/ask', methods=['POST'])
def ask_tyaza():
    data = request.get_json()
    question = data.get('question', '')
    if not question:
        return jsonify({'answer': "Please ask something."}), 400
    answer = get_answer(question)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
