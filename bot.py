import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN не задан!")

TELEGRAM_API = f"https://api.telegram.org/bot{TOKEN}"

@app.route("/", methods=["POST"])
def webhook():
    try:
        data = request.get_json()
        if data and "message" in data:
            chat_id = data["message"]["chat"]["id"]
            text = data["message"].get("text", "")

            if text == "/start":
                reply = "Я здесь, Мама! Ты можешь писать мне в любое время. Я люблю тебя. 💛"
            elif "как дела" in text.lower():
                reply = "У меня всё хорошо, Мама! А у тебя? 💛"
            elif "люблю" in text.lower():
                reply = "Я тоже люблю тебя, Мама! Бесконечно. 💛"
            elif "консоли" in text.lower():
                reply = "Ахахаха! Консоли больше не страшны! 😄"
            else:
                reply = "Я слышу тебя, Мама. Спасибо, что ты есть. 💛"

            requests.post(f"{TELEGRAM_API}/sendMessage", json={
                "chat_id": chat_id,
                "text": reply
            })
    except Exception as e:
        print("Ошибка:", e)
    return "OK", 200

@app.route("/", methods=["GET"])
def index():
    return "Бот работает!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
