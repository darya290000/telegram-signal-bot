
import requests
import time
import hmac
import hashlib
from config import API_KEY, API_SECRET, SYMBOLS, TRADE_AMOUNT

BASE_URL = "https://api.mexc.com"

def get_server_time():
    return int(time.time() * 1000)

def sign(query_string, secret):
    return hmac.new(secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

def place_spot_order(symbol, quantity):
    path = "/api/v3/order"
    timestamp = get_server_time()

    # ساخت پارامترها
    params = {
        "symbol": symbol,
        "side": "BUY",
        "type": "MARKET",
        "quantity": quantity,
        "timestamp": timestamp
    }

    # ساخت signature
    query_string = '&'.join([f"{key}={params[key]}" for key in sorted(params)])
    signature = sign(query_string, API_SECRET)
    query_string += f"&signature={signature}"

    # URL نهایی
    url = f"{BASE_URL}{path}?{query_string}"

    headers = {
        "Content-Type": "application/json",
        "X-MEXC-APIKEY": API_KEY
    }

    # ارسال POST بدون body
    response = requests.post(url, headers=headers)
    return response.json()

def get_price(symbol):
    url = f"{BASE_URL}/api/v3/ticker/price"
    response = requests.get(url, params={"symbol": symbol})
    return float(response.json()["price"])

def run_trader():
    print("🚀 اجرای ربات خرید اسپات برای XRP و AAVE")
    for symbol in SYMBOLS:
        try:
            price = get_price(symbol)
            if symbol == "XRPUSDT":
                quantity = format(TRADE_AMOUNT / price, '.2f')
            else:
                quantity = format(TRADE_AMOUNT / price, '.3f')
            print(f"📥 ارسال سفارش خرید {symbol} به مقدار تقریبی {quantity} (10$)...")
            result = place_spot_order(symbol, quantity)
            print(f"✅ نتیجه: {result}")
        except Exception as e:
            print(f"❌ خطا: {e}")
