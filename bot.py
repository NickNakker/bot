import telebot
from telebot import types
import currencyapicom


bot = telebot.TeleBot('7838750038:AAFnw6cM7jYSvy7DuceiKjKuGfQjiCfiisQ')

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
    client = currencyapicom.Client('cur_live_Ijb19el2Io78pFCjlmYgUyI31Oc6eNBfSAKAjb7z')


    result = client.historical(f'02-02-2021')

    cur = message.text

    if message.text:
        d = result[cur]['value']
        b = result[cur]['code'] + str(d)
        bot.send_message(message.from_user.id, b)


    """
        if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
        """
    

        


bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть