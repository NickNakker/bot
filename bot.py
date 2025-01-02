import telebot
from telebot import types
import currencyapicom

with open('.gitignore', 'r') as data:
    bot = telebot.TeleBot(list(data)[0])
    cur_api_key = list(data)[2]

""""
@bot.message_handler(commands = ['start'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Наш сайт', url='https://habr.com/ru/all/')
    markup.add(btn1)
    bot.send_message(message.from_user.id, "По кнопке ниже можно перейти на сайт хабра", reply_markup = markup)
"""
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    client = currencyapicom.Client(cur_api_key)

    button1 = types.ChatLocation()

    if str(message.text).upper() == '/start'.upper():
        bot.send_message(message.from_user.id, 'Привет, введи текст на латыни')
    
    else:
        try:
            result = client.historical('02-02-2021')

            cur = str(message.text).upper()

            if message.text:
                d = result['data'][cur]['value']
                b = result['data'][cur]['code'] + ' ' + str(d)
                bot.send_message(message.from_user.id, b)
        except:
            bot.send_message(message.from_user.id, 'Нет такой валюты')


        """
            if message.text == "Привет":
            bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
        elif message.text == "/help":
            bot.send_message(message.from_user.id, "Напиши привет")
        else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
            """
    

        


bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть