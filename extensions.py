import requests
from config import currencyapi
import json

class Converter:
    @classmethod
    def convert(self, quote:str, base:str, count:str, keys: dict) -> tuple:  
        if not (base.isalpha() and quote.isalpha()):
            raise BotException('Валюты должны состоять только из букв!')
        try:
            count = float(count)
        except ValueError:
            raise BotException('Некорректно введено число')
        for item in keys.items():
            if quote in item[1]:
                quote = item[0]
            if base in item[1]:
                base = item[0]
        if base not in keys:
            if quote not in keys:
                raise BotException(f'Я не знаю ни {quote}, ни {base}')
            raise BotException(f'Я не знаю данную валюту: {base}')
        if quote not in keys:
            raise BotException(f'Я не знаю данную валюту: {quote}')
        if quote == base:
            raise BotException('Введены одинаковые валюты')
        req = requests.get(f'https://v6.exchangerate-api.com/v6/{currencyapi}/pair/{quote}/{base}')
        price = json.loads(req.content)['conversion_rate']
        amount = round(price*count, 2)
        return quote, base, amount

class BotException(Exception):
    pass

