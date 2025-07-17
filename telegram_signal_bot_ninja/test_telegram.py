import requests


TOKEN = "8136421090:AAFrb8RI6BQ2tH49YXX_5S32_W0yWfT04Cg"
CHAT_ID = "570096331"

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    r = requests.post(url, data=payload)
    if r.status_code == 200:
        print("پیام با موفقیت ارسال شد.")
    else:
        print(f"خطا در ارسال پیام: {r.status_code} - {r.text}")

send_message("سلام! این پیام تست ربات تلگرام است.")
