import time
from config import SYMBOLS
from scalper_signals import analyze_symbol
from telegram_alert import send_alert

history_data = {}

print("📡 ربات سیگنال در حال اجراست...")

while True:
    for symbol in SYMBOLS:
        analyze_symbol(symbol, history_data)
        time.sleep(1)

    time.sleep(30)
