import requests

TOKEN = "8136421090:AAFrb8RI6BQ2tH49YXX_5S32_W0yWfT04Cg"
CHAT_ID = "570096331"
message = "🧪 این یک پیام تستی از ربات شماست."

url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
data = {'chat_id': CHAT_ID, 'text': message}
response = requests.post(url, data=data)

print("Status code:", response.status_code)
print("Response:", response.text)
