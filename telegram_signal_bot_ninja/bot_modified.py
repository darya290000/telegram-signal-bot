
import pytz
from datetime import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# انتخاب منطقه زمانی (مثال: تهران) با pytz
timezone = pytz.timezone("Asia/Tehran")

# نمایش زمان سیستم
async def show_time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    local_time = datetime.now(timezone)  # زمان محلی تهران
    await update.message.reply_text(f"زمان محلی تهران: {local_time}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"سلام! من آماده‌ام!")

if __name__ == '__main__':
    # وارد کردن توکن ربات تلگرام خود
    app = ApplicationBuilder().token('YOUR_BOT_TOKEN').build()

    # اضافه کردن دستورات ربات
    app.add_handler(CommandHandler("time", show_time))
    app.add_handler(CommandHandler("start", start))

    print("🤖 Bot is running...")
    app.run_polling()
