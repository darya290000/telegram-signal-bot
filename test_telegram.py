import requests

# توکن واقعی ربات
TOKEN = "8136421090:AAFrb8RI6BQ2tH49YXX_5S32_W0yWfT04Cg"

# آیدی عددی چت (مثلاً آیدی تلگرام خودت)
CHAT_ID = "570096331"

message = "سلام! این یک پیام تستی از کد پایتون است."

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
data = {'chat_id': CHAT_ID, 'text': message}

response = requests.post(url, data=data)
print(response.status_code, response.text)
