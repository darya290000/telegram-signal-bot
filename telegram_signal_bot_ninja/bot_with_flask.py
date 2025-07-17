import pytz
from datetime import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from flask import Flask
from threading import Thread

# انتخاب منطقه زمانی (مثال: تهران) با pytz
timezone = pytz.timezone("Asia/Tehran")

# دستور نمایش زمان
async def show_time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    local_time = datetime.now(timezone)  # زمان محلی تهران
    await update.message.reply_text(f"زمان محلی تهران: {local_time}")

# دستور شروع
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"سلام! من آماده‌ام!")

# راه‌اندازی Flask برای نگهداری ربات آنلاین
app = Flask('')

@app.route('/')
def home():
    return "ربات آنلاین است ✅"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == '__main__':
    # وارد کردن توکن ربات تلگرام خود
    app = ApplicationBuilder().token('YOUR_BOT_TOKEN').build()
    
    # اضافه کردن دستورات ربات
    app.add_handler(CommandHandler("time", show_time))
    app.add_handler(CommandHandler("start", start))

    # شروع نگهداری ربات آنلاین
    keep_alive()

    print("🤖 Bot is running...")
    app.run_polling()
