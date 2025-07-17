import requests
from config import SYMBOL, INTERVAL, LIMIT

def get_klines():
    url = f"https://api.mexc.com/api/v3/klines?symbol={SYMBOL}&interval={INTERVAL}&limit={LIMIT}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data  # لیست لیست کندل‌ها
    except Exception as e:
        print(f"[❌] خطا در دریافت کندل‌ها: {e}")
        return None
