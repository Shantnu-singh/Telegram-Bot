import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.ext import Updater , CommandHandler , ContextTypes , ApplicationBuilder
Token = "7609744932:AAEKZUVfVqg3owANN_ED1XzI5OX9D*****"

# hello function
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
    
# Define the async function for the bot command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hey, Welcome to my bot. you must be {update.effective_user.first_name} with last name{update.effective_user.last_name}')
   
   
app = ApplicationBuilder().token(Token).build()

# Add the hello command handler
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("start", start))

# Start the bot
app.run_polling()