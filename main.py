import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

from heroes import get_hero  # Keep this import for the hero command
from match import get_last_match  # Import the function to get matches

load_dotenv()

# Start command handler
async def startHandler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Use /hero <id> to get information about a hero, and /match <player_id> to get the most recent match.")

# Hero command handler
async def heroHandler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    hero_id = int(context.args[0])
    response_size = context.args[1] if len(context.args) > 1 else None
    hero = get_hero(hero_id)
    if hero:
        if response_size == "full":
            await update.message.reply_text(hero.to_long_message())
        else:
            await update.message.reply_text(hero.to_message())
    else:
        await update.message.reply_text("Hero not found.")

# Match command handler
async def matchHandler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("Please provide a player ID. Usage: /match <player_id>")
        return
    
    player_id = context.args[0]  # Get player ID from user input
    match = get_last_match(player_id)  # Fetch recent match

    if match:
        # Format and send match info to the user
        match_info = (f"Match ID: {match['match_id']}\n"
                      f"Hero ID: {match['hero_id']}\n"
                      f"Radiant Win: {'Yes' if match['radiant_win'] else 'No'}\n"
                      f"Duration: {match['duration']} seconds")
        await update.message.reply_text(match_info)
    else:
        await update.message.reply_text("No recent match found or failed to fetch match details.")

# Set up the application and add handlers
app = ApplicationBuilder().token(os.getenv("TELEGRAM_API_TOKEN")).build()

# Add handlers for both /hero and /match commands
app.add_handler(CommandHandler("start", startHandler))
app.add_handler(CommandHandler("hero", heroHandler))  # Keep heroHandler for hero information
app.add_handler(CommandHandler("match", matchHandler))  # Add matchHandler for match info

# Start the bot
print("Bot is running...")
app.run_polling()
print("Bot is stopped.")
