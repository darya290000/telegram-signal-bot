from telegram import Bot
import requests

# === اطلاعات ربات ===
TOKEN = '8136421090:AAFrb8RI6BQ2tH49YXX_5S32_W0yWfT04Cg'
CHAT_ID = '570096331'

# === تابع ارسال پیام ===
def send_signal(message):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    data = {
        'chat_id': CHAT_ID,
        'text': message
    }
    response = requests.post(url, data=data)
    print("✅ سیگنال ارسال شد:", response.status_code)

# === تست اولیه ===
if __name__ == "__main__":
    send_signal("🚀 تست موفق! ربات شما کار می‌کند.")
