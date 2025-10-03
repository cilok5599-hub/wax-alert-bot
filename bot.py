from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import config
import price, alerts, tx, drops

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to Wax Alert Bot!\n\n"
        "With this bot, you can:\n"
        "🔔 Get real-time WAX price alerts\n"
        "📈 Track large blockchain transactions\n"
        "🎁 Receive updates on drops & staking events\n\n"
        "Type /help to begin 🚀"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 Available commands:\n\n"
        "/start - Welcome message\n"
        "/help - Show this help\n"
        "/price - Latest WAX price + chart (source: Coingecko)\n"
        "/alerts - Set price alerts\n"
        "/tx - Track large blockchain transactions (source: Waxblock.io)\n"
        "/drops - View NFT drops & top collections (source: Neftyblocks)\n\n"
        "⚠️ Note: If bot is not responding, the server might be offline 🙏"
    )

def main():
    app = Application.builder().token(config.BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("price", price.get_price))
    app.add_handler(CommandHandler("alerts", alerts.set_alert))
    app.add_handler(CommandHandler("tx", tx.get_large_transactions))
    app.add_handler(CommandHandler("drops", drops.get_drops))

    print("✅ Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
