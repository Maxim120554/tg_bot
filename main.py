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


@dp.message_handler(commands=['start', 'help'])
async def answer_start(message: types.Message):
    if message.text == '/start':
        user = User(message.from_user.first_name, message.from_user.last_name, message.from_user.id)
        if message.from_user.id not in ids:
            database[message.from_user.id] = user
        await bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}')
    print(f'{message.from_user.first_name} написал: {message.text}')


@dp.message_handler()
async def answer(message: types.Message):
    await get_info(bot=bot, message=message)




def main():
    executor.start_polling(dp, skip_updates=True)   # не отвечает на сообщения, когда бот был не онлайн


if __name__ == '__main__':
    main()