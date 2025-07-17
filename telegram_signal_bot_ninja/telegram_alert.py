import requests
from config import TOKEN, CHAT_ID

def send_alert(message: str):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML"}
    try:
        resp = requests.post(url, data=data)
        resp.raise_for_status()
        print("[✅] پیام با موفقیت ارسال شد.")
    except requests.exceptions.RequestException as e:
        print(f"[❌] خطا در ارسال پیام به تلگرام: {e}")
