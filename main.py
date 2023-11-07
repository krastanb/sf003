import telebot
from helper import APIException

TOKEN = "6543802194:AAF9Ysom8rgKeNJp-ZZ0cP5HCC2TQNrHPHo"

bot = telebot.TeleBot(TOKEN)

keys = {'USD': ('доллар', 'долларов', 'доллара', 'dollar', 'dollar', 'usd'),
        'EUR': ('евро', 'euro', 'euros', 'eur'),
        'RUB': ('рубль', 'рублей', 'рубля', 'rub', 'rubles', 'ruble'),
        'BTC': ('btc', 'bitcoin', 'bitcoins', 'биткойн', 'биткойнов', 'биткойна')}

@bot.message_handler(commands=['start', 'help'])
def start_help(message):
    bot.reply_to(message, 'Введите <имя валюты> <в какую валюту перевести> <количество>\
                                       \nНапример: btc рубль 0.1\
                           \nПосмотреть список доступных валют: /values')

@bot.message_handler(commands=['values'])
def values(message):
    s = 'Список доступных валют и их вариации написания:\n'
    for k, v in keys.items():
        s+=f"{k} | {', '.join(v)} \n"
    bot.reply_to(message, s)

@bot.message_handler(content_types=['text'])
def base(message):
    bot.reply_to(message, 'ok')

@bot.message_handler(content_types=['audio', 'photo', 'voice', 'video', 'document', 'location', 'contact', 'sticker'])
def errors(message):
    pass 


bot.polling(none_stop=True) 