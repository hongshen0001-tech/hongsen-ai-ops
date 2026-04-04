from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def ask_ai(prompt):
    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "你是企业级AI运维专家"},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    return response.json()

@app.route("/")
def home():
    return "🚀 鸿森智汇 AI 运维系统已运行"

@app.route("/ai", methods=["POST"])
def ai():
    data = request.json
    prompt = data.get("prompt", "分析当前系统状态")

    result = ask_ai(prompt)

    return jsonify(result)

@app.route("/auto")
def auto():
    prompt = "分析服务器CPU、内存、网络并给出优化建议"
    result = ask_ai(prompt)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
