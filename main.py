import telebot
from extensions import BotException, Converter
from config import TOKEN, keys

bot = telebot.TeleBot(TOKEN)
        
@bot.message_handler(commands=['start', 'help'])
def start_help(message):
    bot.reply_to(message, 'Введите <имя валюты> <в какую валюту перевести> <количество>\
                                       \nНапример: usd рубль 10\
                           \nПосмотреть список доступных валют: /values')

@bot.message_handler(commands=['values'])
def values(message):
    s = 'Список доступных валют и их вариации написания:\n'
    for k, v in keys.items():
        s+=f"{k} | {', '.join(v)} \n"
    bot.reply_to(message, s)

@bot.message_handler(content_types=['text'])
def convert(message):
    try:
        values = message.text.lower().split()
        if len(values)!=3:
            raise BotException('Введено некорректное число параметров')
        quote, base, count = values
        quote, base, amount = Converter.convert(quote, base, count, keys)
    except BotException as e:
        bot.reply_to(message, f"{e}")
    except Exception as e: # там ограниченное количетсво запросов в минуту, может выдавать ошибку 
        print(e)
        bot.reply_to(message, 'Ошибка со стороны сервера! Ожидайте, мы уже решаем данную проблему!')
    else:
        bot.reply_to(message, f"{count} {quote} = {amount} {base}")
    

@bot.message_handler(content_types=['audio', 'photo', 'voice', 'video', 'document', 'location', 'contact', 'sticker'])
def errors(message):
    bot.reply_to(message, "К сожалению, я не могу обработать данное сообщение")


bot.polling(none_stop=True) 