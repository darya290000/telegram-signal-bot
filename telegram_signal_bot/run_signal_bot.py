import time
from config import SYMBOLS
from scalper_signals import analyze_symbol
from telegram_alert import send_alert

print("📡 ربات سیگنال‌دهنده در حال اجراست...")

while True:
    for symbol in SYMBOLS:
        try:
            signal = analyze_symbol(symbol)
            if signal:
                send_alert(signal)
                print(f"[✅] سیگنال ارسال شد: {signal}")
            else:
                print(f"[⚠️] سیگنال برای {symbol} دریافت نشد.")
        except Exception as e:
            print(f"[❌] خطا در تحلیل یا ارسال سیگنال {symbol}: {e}")
        time.sleep(1)  # فاصله کم بین هر درخواست

    time.sleep(30)  # بعد از بررسی همه نمادها ۳۰ ثانیه صبر کن
