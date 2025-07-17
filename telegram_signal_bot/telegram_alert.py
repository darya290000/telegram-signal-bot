import requests
from config import TOKEN, CHAT_ID

def send_alert(message):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': message}
    try:
        response = requests.post(url, data=data, timeout=10)
        response.raise_for_status()  # اگه خطایی بود، پرتاب کنه
        print(f"[✅] سیگنال ارسال شد: {message}")
    except requests.exceptions.RequestException as e:
        print(f"[❌] خطا در ارسال پیام به تلگرام: {e}")
