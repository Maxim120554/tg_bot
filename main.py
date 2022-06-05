from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from Users import *
from Functions import *

import os


TOKEN = '5533902111:AAE5BfjCHyKnrq1hziubvzOpg6901WAZflM'
ids = []
database = {}
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
commands = ['start', 'help', 'add_favorites', 'clear_favorites', 'show_favorites']


@dp.message_handler(commands=commands)
async def answer_start(message: types.Message):
    if message.from_user.id not in ids:
        user = User(message.from_user.first_name, message.from_user.last_name, message.from_user.id)
        database[message.from_user.id] = user
    if message.text == '/start':
        await bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}')
    elif message.text == '/help':
        await bot.send_message(message.from_user.id, 'Отправьте мне название монеты и узнаете основную информацию о ней')
    elif message.text == '/add_favorites':
        database[message.from_user.id].is_add_favorites = True
        await bot.send_message(message.from_user.id, 'Перечислите через пробел монеты, которые хотите добавить в ИЗБРАННОЕ')
    elif message.text == '/clear_favorites':
        database[message.from_user.id].favorites.clear()
        await bot.send_message(message.from_user.id, 'Избранные монеты удалены')
    elif message.text == '/show_favorites':
        await bot.send_message(message.from_user.id, f'{database[message.from_user.id].favorites}')

    print(f'{message.from_user.first_name} написал: {message.text}')




@dp.message_handler()
async def answer(message: types.Message):
    if message.from_user.id not in ids:
        user = User(message.from_user.first_name, message.from_user.last_name, message.from_user.id)
        database[message.from_user.id] = user
    elif database[message.from_user.id].is_add_favorites:
        database[message.from_user.id].is_add_favorites = False
        array = message.text.split(' ')
        for item in array:
            if item not in database[message.from_user.id].favorites:
                database[message.from_user.id].favorites.append(item.lower())
        await bot.send_message(message.from_user.id, 'Монеты добавлены в ИЗБРАННОЕ')

    if not database[message.from_user.id].is_add_favorites:
        await get_info(bot=bot, message=message)




def main():
    executor.start_polling(dp, skip_updates=True)   # не отвечает на сообщения, когда бот был не онлайн


if __name__ == '__main__':
    main()