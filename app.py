from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(
    api_key="AIzaSyC5bGY6zzld-pERmsvFbJeI6ZDjzM1uzw0",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

history = [{'role': 'system', 'content': 'You are an AI chatbot from the year 2080. Your name is Abhishek Bot.'}]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/get', methods=['POST'])
def get_bot_response():
    user_input = request.json['message']
    history.append({'role': 'user', 'content': user_input})

    response = client.chat.completions.create(
        model="gemini-2.0-flash",
        n=1,
        messages=history
    )
    reply = response.choices[0].message.content
    history.append({'role': 'assistant', 'content': reply})
    return jsonify({'reply': reply})

@app.route('/ping')
def ping():
    return "pong"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
