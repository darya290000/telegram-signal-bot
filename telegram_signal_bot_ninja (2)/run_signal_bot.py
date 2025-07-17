import time
from config import SYMBOLS
from scalper_signals import analyze_symbol
from telegram_alert import send_alert

history_data = {}

print("📡 ربات سیگنال‌دهنده در حال اجراست...")

while True:
    for symbol in SYMBOLS:
        signal = analyze_symbol(symbol, history_data)
        if signal:
            send_alert(signal)
    time.sleep(30)  # هر 30 ثانیه یکبار بررسی شود
