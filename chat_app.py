from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

API_URL = "http://<youriphere>:8000/v1/completions"
MODEL_NAME = "fdtn-ai/Foundation-Sec-8B"

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json["prompt"]
    payload = {
        "model": MODEL_NAME,
        "prompt": user_input,
        "max_tokens": 300
    }
    try:
        response = requests.post(API_URL, json=payload, timeout=60)
        response.raise_for_status()
        result = response.json()["choices"][0]["text"]
        return jsonify({"response": result})
    except Exception as e:
        return jsonify({"response": f"[ERROR] {e}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
