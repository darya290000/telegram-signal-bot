import requests
from config import TOKEN, CHAT_ID

def send_alert(message):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': message}
    requests.post(url, data=data)
    print(f"[✅] پیام ارسال شد: {message}")
