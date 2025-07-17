import requests
import os

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)

def handle_update(update):
    message = update.get("message", {})
    text = message.get("text", "")
    chat_id = message.get("chat", {}).get("id", "")

    if not text or not chat_id:
        return

    if text == "/start":
        send_message(chat_id, "👋 خوش آمدید به ربات سیگنال‌دهی مالی!")
    elif text == "/subscribe":
        send_message(chat_id, "✅ شما با موفقیت در دریافت سیگنال‌ها عضو شدید.")
    elif text == "/help":
        send_message(chat_id, "📘 راهنما:\n/start\n/subscribe\n/unsubscribe\n/status")
    elif text == "/status":
        send_message(chat_id, "📡 شما در حال حاضر عضو هستید.")
    elif text == "/unsubscribe":
        send_message(chat_id, "❌ عضویت شما لغو شد.")
    else:
        send_message(chat_id, "🤖 دستور نامعتبر است. از /help استفاده کنید.")