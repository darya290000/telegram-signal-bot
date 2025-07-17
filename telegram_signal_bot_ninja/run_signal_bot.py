import time
from mexc_api import get_klines
from scalper_signals import analyze_candles
from telegram_alert import send_alert

print("🚀 ربات اسکالپینگ MEXC شروع به کار کرد...")

while True:
    klines = get_klines()
    signal = analyze_candles(klines)
    if signal:
        send_alert(signal)
    time.sleep(5)  # هر 5 ثانیه یک بار چک شود
