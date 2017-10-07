#!/usr/bin/python3
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import logging
import misc
from weather import get_weather


logger = logging.getLogger(__name__)
token = misc.token

def start(bot, update):
    update.message.reply_text('Я покажу тебе погоду в любой точке мира, в момент запроса. Начнем?')
    """keyboard = [InlineKeyboardButton("Option 1", callback_data='1'),
                InlineKeyboardButton("Option 2", callback_data='2')],

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Выберите', reply_markup=reply_markup)"""

def button(bot, update):
    query = update.callback_query

    bot.edit_message_text(text="Selected option: %s" % query.data,
                          chat_id=query.message.chat_id,
                          message_id=query.message.chat_id)

def help(bot, update):
    update.message.reply_text("Use /start to test this bot.")

def echo(bot, update):
    update.message.reply_text(get_weather(update.message.text))




def main():
    #Token
    updater = Updater(token)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    dp.add_handler(CallbackQueryHandler(button))

    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_handler(CommandHandler('help', help))

    updater.start_polling()

    #updater.idle()




if __name__ == '__main__':
    main()