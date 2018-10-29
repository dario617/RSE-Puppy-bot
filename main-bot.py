#! /usr/bin/env python3
from telegram.ext import Updater, CommandHandler
import mytoken
import logging

global subscribed_users
subscribed_users = list()

TIME_INTERVAL_SECS = 5
PUPPY_ADDRESS = "200.7.6.134"

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    # Run bot
    updater = Updater(mytoken.TOKEN)

    # Say hello!
    updater.dispatcher.add_handler(CommandHandler('hello', hello))
    updater.dispatcher.add_handler(CommandHandler('subscribe',subscribe,
                                                pass_job_queue=True))
    updater.start_polling()
    updater.idle()

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def checkPuppy(bot, job):
    for chat in subscribed_users:
        bot.send_message(chat,text="Checked on puppy")

def subscribe (bot, update, job_queue):
    chat_id = update.message.chat_id
    subscribed_users.append(chat_id)
    update.message.reply_text('Subscribed to check on Cute Puppy!'+str(subscribed_users))
    job_queue.run_once(checkPuppy,TIME_INTERVAL_SECS,context=chat_id)

if __name__ == "__main__":
    main()