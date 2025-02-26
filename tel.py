import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext

# 📌 اطلاعات ربات
TOKEN = "7802634942:AAHHOUSh27rDU0gWYGF0UZhdbqhfk-Yvde8"  

# 📌 شناسه کانال‌ها و لینک‌های آن‌ها
CHANNELS = {
    "فیلم و سریال ایرانی": "https://t.me/boomrang_irani",
    "فیلم خارجی": "https://t.me/boomrang_asli",
    "سریال خارجی": "https://t.me/Boomrang_serial",
    "انیمیشن": "https://t.me/boomrang_anim"
}

# ⚙️ تنظیمات لاگ‌گیری
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# 🎬 نمایش دکمه‌های دسته‌بندی
async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [[InlineKeyboardButton(name, url=url)] for name, url in CHANNELS.items()]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🎥 لطفاً یک دسته‌بندی را انتخاب کنید:", reply_markup=reply_markup)

# 🎯 اجرای بات
def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))

    print("✅ بات فعال شد!")
    app.run_polling()

if __name__ == "__main__":
    main()