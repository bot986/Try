from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Your bot token from @BotFather
BOT_TOKEN = "Your_bot_token"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey! I'm alive and working!")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
