#! /usr/bin/env python3
import json
import logging
from telegram.ext import Updater, CommandHandler
import mytoken, check


TIME_INTERVAL_SECS = 5
PUPPY_ADDRESS = "http://200.7.6.134"


def main():
    # Run bot
    updater = Updater(mytoken.TOKEN)

    # Say hello!
    updater.dispatcher.add_handler(CommandHandler('hello', hello))
    updater.dispatcher.add_handler(CommandHandler('subscribe',subscribe,
                                                pass_job_queue=True))
    updater.job_queue.run_repeating(check_puppy, interval=30, first=10)

    updater.start_polling()
    updater.idle()


def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))
    logging.info("User {} said hello!".format(update.message.from_user.first_name))


def subscribe(bot, update):
    chat_id = update.message.chat_id
    if chat_id not in data['subs_ids']:
        data['subs_ids'].append(chat_id)
        json.dump(data, open("data.json","w"))
        update.message.reply_text('Subscribed to check on Cute Puppy!')
        logging.info("Chat id {} has subscribed".format(update.message.chat_id))
    else:
        update.message.reply_text('Already subscribed to check on Cute Puppy!')
        logging.info("Chat id {} has attempted to resubscribe".format(update.message.chat_id))


def check_puppy(bot, job):
    global last_status_ok
    current_status_ok, msg = check.check_url(PUPPY_ADDRESS)

    if current_status_ok is not last_status_ok:
        for chat_id in data['subs_ids']:
            if not current_status_ok:
                bot.send_message(chat_id = chat_id, text = "{} is down!".format(PUPPY_ADDRESS))
            else:
                bot.send_message(chat_id = chat_id, text = "{} is up!".format(PUPPY_ADDRESS))

    last_status_ok = current_status_ok
    logging.info("Status check done!")


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    with open("data.json", "r") as file:
        data = json.load(file)
    # last_check_time = None
    last_status_ok = None
    main()
