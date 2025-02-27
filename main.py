import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler

from dotenv import load_dotenv
load_dotenv()

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("Message from ", update.effective_user.username, ": ", update.message.text)
    # Check if the message is in a group chat
    if update.message.chat.type != 'group':
        await update.message.reply_text(f'Hello {update.effective_user.first_name}')

app = ApplicationBuilder().token(os.getenv("TELEGRAM_API_TOKEN")).build()

print("Bot is running...")
app.add_handler(MessageHandler(None, hello))

app.run_polling()
print("Bot is stopped.")