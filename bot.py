import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.ext import Updater , CommandHandler , ContextTypes , ApplicationBuilder
import secretes
import artical_in_db

Token = secretes.Telegram_Token
 
# hello function
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
    
# Define the async function for the bot command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hey, Welcome to my bot. you must be {update.effective_user.first_name} with last name{update.effective_user.last_name}')

async def help(update: Update , context: ContextTypes.DEFAULT_TYPE)-> None:
    await update.message.reply_text(
            """/hello -> Welcome users
              /start -> Start the Processes
              /help  -> This particular Message
              /articles -> Get two Articles With link and summary"""
              )
    
async def help(update: Update , context: ContextTypes.DEFAULT_TYPE)-> None:
    pass
   
app = ApplicationBuilder().token(Token).build()

# Add the hello command handler
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help" , help))

# Start the bot
app.run_polling()