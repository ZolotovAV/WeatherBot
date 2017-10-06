#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import json




def get_weather(text):
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + text + '&appid=ce64b6f1cc92168405d48b784d0112e4&lang=ru&units=metric'

    response = requests.get(url).json()
    error = 'Город не найден.'
    error_pic = 'Пиши текст.'



    """Ниже обработка исключения с несовпадающим возвратом запроса ['request']"""

    try:
        weather = response['name'] + '  ' + response['sys']['country'] + '\n' + 'От ' + str(response['main']['temp_min'])\
                  + '°C' + ' до ' + str(response['main']['temp_max']) + '°C' + '  ' + response['weather'][-1]['description']
    except KeyError:
        return error
    else:
        return weather


    try:
        weather != response['name'] + '  ' + response['sys']['country'] + '\n' + 'От ' + str(response['main']['temp_min'])\
                  + '°C' + ' до ' + str(response['main']['temp_max']) + '°C' + '  ' + response['weather'][-1]['description']
    except KeyError:
        return error_pic









"""
Запуск сбора инфы в json.

def main():
    d = get_weather("Samara")

    with open('openweathermap.json', 'w') as file:
        json.dump(d, file, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()
"""

