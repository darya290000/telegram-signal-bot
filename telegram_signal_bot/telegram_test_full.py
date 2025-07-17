import requests

TOKEN = "8136421090:AAFrb8RI6BQ2tH49YXX_5S32_W0yWfT04Cg"
CHAT_ID = "570096331"

def get_price(symbol):
    url = f"https://api.mexc.com/api/v3/ticker/price?symbol={symbol}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        price = float(data["price"])
        print(f"قیمت {symbol} دریافت شد: {price}")
        return price
    except Exception as e:
        print(f"❌ خطا در دریافت قیمت {symbol}: {e}")
        return None

def analyze_symbol(symbol):
    price = get_price(symbol)
    if price is None:
        return None
    if int(price) % 2 == 0:
        signal = f"🟢 سیگنال خرید: {symbol} | قیمت: {price}"
    else:
        signal = f"🔴 سیگنال فروش: {symbol} | قیمت: {price}"
    print(f"سیگنال ساخته شد: {signal}")
    return signal

def send_alert(message):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': message}
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
        print(f"[✅] سیگنال ارسال شد: {message}")
    except requests.exceptions.RequestException as e:
        print(f"[❌] خطا در ارسال پیام به تلگرام: {e}")

if __name__ == "__main__":
    symbol = "BTCUSDT"  # می‌توانید به دلخواه عوض کنید
    signal = analyze_symbol(symbol)
    if signal:
        send_alert(signal)
