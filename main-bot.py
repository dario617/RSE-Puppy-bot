#! /usr/bin/env python3
from telegram.ext import Updater, CommandHandler
import mytoken


def main():
    updater = Updater(mytoken.TOKEN)
    updater.dispatcher.add_handler(CommandHandler('hello', hello))
    updater.start_polling()
    updater.idle()


def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


if __name__ == "__main__":
    main()
