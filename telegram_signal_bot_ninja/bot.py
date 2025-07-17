import json
import hmac
import hashlib
import time
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import config  # بارگذاری تنظیمات از فایل config.py

BASE_URL = "https://api.mexc.com"

def sign(params: dict) -> str:
    query = "&".join([f"{key}={params[key]}" for key in sorted(params)])
    signature = hmac.new(config.API_SECRET.encode(), query.encode(), hashlib.sha256).hexdigest()
    return signature

def place_order(symbol: str, side: str, quantity: float = 10.0):
    endpoint = "/api/v3/order"
    url = BASE_URL + endpoint

    timestamp = int(time.time() * 1000)
    params = {
        "symbol": symbol,
        "side": side.upper(),
        "type": "MARKET",
        "quantity": quantity,
        "timestamp": timestamp
    }
    params["signature"] = sign(params)

    headers = {
        "X-MEXC-APIKEY": config.API_KEY
    }

    response = requests.post(url, params=params, headers=headers)
    return response.json()

async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        symbol = context.args[0].upper()
        res = place_order(symbol, "BUY")
        await update.message.reply_text(f"📈 خرید انجام شد:\n{res}")
    except Exception as e:
        await update.message.reply_text(f"خطا: {str(e)}")

async def sell(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        symbol = context.args[0].upper()
        res = place_order(symbol, "SELL")
        await update.message.reply_text(f"📉 فروش انجام شد:\n{res}")
    except Exception as e:
        await update.message.reply_text(f"خطا: {str(e)}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(config.TOKEN).build()  # استفاده از توکن تلگرام از config
    app.add_handler(CommandHandler("buy", buy))
    app.add_handler(CommandHandler("sell", sell))
    print("🤖 Bot is running...")
    app.run_polling()
if __name__ == '__main__':
    app = ApplicationBuilder().token('8136421090:AAFrb8RI6BQ2tH49YXX_5S32_W0yWfT04Cg').build()

    # اضافه کردن دستورات
    app.add_handler(CommandHandler("time", show_time))
    app.add_handler(CommandHandler("start", start))

    # استفاده از Flask برای نگه داشتن ربات آنلاین (اگر استفاده می‌کنید)
    keep_alive()

    print("🤖 ربات در حال اجرا است...")
    app.run_polling()  # این متد صحیح برای اجرای ربات است
