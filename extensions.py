import requests
import json
from config import keys

class ConvertionExeption(Exception):
    pass

class Converter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
           raise ConvertionExeption(f'Невозможно перевести одинаковые валюты{base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {base}')
        try:
            amount = int(amount)
        except ValueError:
            raise ConvertionExeption(f'Не удалось обработать количество {amount}')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = float(json.loads(r.content)[keys[base]])
        return total_base * amount
