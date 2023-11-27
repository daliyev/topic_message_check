from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with the actual token you get from BotFather on Telegram
TOKEN = '6469806612:AAFWmP0wvBebxJJ196K392AfN6jguZJgJNc'

# Replace 'GROUP_ID' with the ID of your group
GROUP_ID = 1782638193  # Replace with your actual group ID

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Assalomu alaykum! Bot ishga tushdi.')


def delete_photo(update: Update, context: CallbackContext) -> None:
    message = update.message
    print("delete keldi")

    # Check if the message has a photo and the topic is "Yozuvlar"
    if message.text and message.message_thread_id == 68:
        print("if ni ichi")

        # Delete the message
        mid = message.message_id
        context.bot.delete_message(chat_id=message.chat_id, message_id=mid)

def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add a start command handler
    dp.add_handler(CommandHandler("start", start))

    # Add a message handler to delete photos in the "Yozuvlar" topic
    dp.add_handler(MessageHandler(Filters.text, delete_photo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal (Ctrl+C) to stop it
    updater.idle()

if __name__ == '__main__':
    main()
