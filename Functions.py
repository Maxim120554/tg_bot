from aiogram import Bot, types
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
from main import bot


async def get_info(bot: Bot, message: types.Message):
    ua = UserAgent()
    headers = {
        'accept': '* / *',
        'UserAgent': ua.random
    }
    try:
        req = requests.get(f'https://coinmarketcap.com/currencies/{message.text.lower()}/markets/', headers=headers)
        soup = BeautifulSoup(req.text, 'lxml')
        symbol = soup.find('small', class_='nameSymbol').text
        price = soup.find('div', class_='priceValue').text
        market_cap = soup.find('div', class_='statsValue').text
        max_supply = soup.find_all('div', class_='maxSupplyValue')[0].text
        total_supply = soup.find_all('div', class_='maxSupplyValue')[1].text
        await bot.send_message(message.chat.id, f'{symbol}\nЦена: {price}\nКапитализация: {market_cap}\nМаксимальное количество: {max_supply}\nТекущее количество: {total_supply}')
    except requests.exceptions.MissingSchema:
        await bot.send_message(message.chat.id, 'Введите корректное название')
    except AttributeError:
        await bot.send_message(message.chat.id, 'Введите корректное название')
