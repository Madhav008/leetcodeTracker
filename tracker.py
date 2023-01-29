from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes,MessageHandler


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name} Please provide your profile information')

def repeat_message(update, context):
    message = update.message.text
    context.bot.send_message(chat_id=update.message.chat_id, text=message)

    , 
app = ApplicationBuilder().token("1643625140:AAHpkVELtF5zgCT9m6_Hc2ZaTvSANesKj64").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("repeat", repeat_message))

app.run_polling()
