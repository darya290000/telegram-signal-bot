# scalper_signals.py

import requests

def get_price(symbol):
    """
    دریافت قیمت لحظه‌ای برای یک symbol از API صرافی MEXC
    """
    url = f"https://api.mexc.com/api/v3/ticker/price?symbol={symbol}"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        return float(data["price"])
    except Exception as e:
        print(f"❌ خطا در دریافت قیمت {symbol}: {e}")
        return None

def analyze_symbol(symbol):
    """
    تحلیل نماد و ساخت سیگنال خرید یا فروش بر اساس الگوریتم تستی
    (می‌توان در آینده به استراتژی واقعی مانند EMA یا RSI ارتقا داد)
    """
    price = get_price(symbol)
    if price is None:
        return None

    # الگوریتم تستی ساده: اعداد زوج = خرید، فرد = فروش (صرفاً جهت تست پیام‌دهی)
    if int(price) % 2 == 0:
        signal = f"🟢 سیگنال خرید: {symbol} | قیمت: {price}"
    else:
        signal = f"🔴 سیگنال فروش: {symbol} | قیمت: {price}"

    return signal
