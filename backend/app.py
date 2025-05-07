from flask import Flask, request, jsonify, render_template
from openai_service import get_openai_response
from dotenv import load_dotenv
from flask_cors import CORS
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    if not user_message:
        return jsonify({"error": "mensagem vaziam"}), 400
    
    try:
        reply = get_openai_response(user_message)
        return jsonify({"reply": reply})
    except Exception as e:
        print(f"Erro interno: {e}")
        return jsonify({"error": "Erro ao processar a resposta."})
if __name__ =='__main__':
    
    app.run()
