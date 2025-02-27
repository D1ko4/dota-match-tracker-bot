import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler

from heroes import get_hero

from dotenv import load_dotenv
load_dotenv()

async def startHandler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Use /hero <id> to get information about a hero.")

async def heroHandler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    hero_id = int(context.args[0])
    hero = get_hero(hero_id)
    if hero:
        await update.message.reply_text(hero.to_message())
    else:
        await update.message.reply_text("Hero not found.")

app = ApplicationBuilder().token(os.getenv("TELEGRAM_API_TOKEN")).build()

print("Bot is running...")
app.add_handler(CommandHandler("start", startHandler))
app.add_handler(CommandHandler("hero", heroHandler))

app.run_polling()
print("Bot is stopped.")