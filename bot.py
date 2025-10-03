from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "7778419950:AAGXPsToJurFL0uCaB9Ta7bwk50YKl8hQ5M" 

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"Hello {user.first_name}! 👋\n"
        f"Welcome to Wax Alert Bot.\n\n"
        f"Available commands:\n"
        f"/start - Start the bot\n"
        f"/help - Show help and usage\n"
        f"/alert - Set a custom alert"
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("🚀 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
