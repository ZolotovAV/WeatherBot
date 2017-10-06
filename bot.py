#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import misc
from weather import get_weather
from time import sleep
import json


token = misc.token

# https://api.telegram.org/bot"Ваш token Telegram"/sendmessage?chat_id=292543111&text=hi
URL = 'https://api.telegram.org/bot' + token + '/'


global last_update_id
last_update_id = 0




def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


def start_help():
    pass


def get_message():
    data = get_updates()

    last_object = data['result'][-1]
    current_update_id = last_object['update_id']

    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id

        chat_id = last_object['message']['chat']['id']
        message_text = last_object['message']['text']
        if message_text != last_object['message']['text']:
            return 'Пиши текст'
        else:
            message = {'chat_id': chat_id, 'text': message_text}
            return message

    return None


def send_message(chat_id, text='Момент'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)


def error_message(chat_id, text):
    pass


def main():
#    d = get_updates()

#    with open('updates.json', 'w') as file:
#        json.dump(d, file, indent=2, ensure_ascii=False)
    while True:
        answer = get_message()

        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']

            if text == '/Start':
                send_message(chat_id, 'Данный бот показывает погоду в любой точке мира в момент запроса, вызовите /Help')
            elif text == '/Help':
                send_message(chat_id, 'Принимаются команды только на латинице - Samara')
            elif text == text:
                send_message(chat_id, get_weather(text))

        else:
            continue






if __name__ == '__main__':
    main()
