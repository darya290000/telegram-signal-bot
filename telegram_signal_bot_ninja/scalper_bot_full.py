
import requests
import pandas as pd
import time
import ta
from config import SYMBOL, INTERVAL, LIMIT, TAKE_PROFIT, STOP_LOSS
from telegram_alert import send_alert

def get_candles(symbol, interval, limit):
    url = f"https://api.mexc.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    try:
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame(data, columns=[
            "timestamp", "open", "high", "low", "close", "volume", "close_time", "quote_volume"
        ])
        df["close"] = df["close"].astype(float)
        return df
    except Exception as e:
        print(f"[❌] خطا در دریافت کندل‌ها: {e}")
        return None

def analyze(df):
    try:
        # محاسبه اندیکاتورها
        rsi = ta.momentum.RSIIndicator(df["close"]).rsi()
        macd_line = ta.trend.macd(df["close"])
        macd_signal = ta.trend.macd_signal(df["close"])
        macd_hist = macd_line - macd_signal

        last_close = df["close"].iloc[-1]
        last_rsi = rsi.iloc[-1]
        last_macd = macd_line.iloc[-1]
        last_signal = macd_signal.iloc[-1]

        signal = None

        if last_rsi < 30 and last_macd > last_signal:
            signal = f"🟢 سیگنال خرید: {SYMBOL} | قیمت: {last_close}"
        elif last_rsi > 70 and last_macd < last_signal:
            signal = f"🔴 سیگنال فروش: {SYMBOL} | قیمت: {last_close}"

        return signal
    except Exception as e:
        print(f"[❌] خطا در تحلیل تکنیکال: {e}")
        return None

print("🚀 ربات اسکالپینگ MEXC شروع به کار کرد...")

while True:
    df = get_candles(SYMBOL, INTERVAL, LIMIT)
    if df is not None:
        signal = analyze(df)
        if signal:
            print(f"[✅] {signal}")
            send_alert(signal)
    time.sleep(5)
