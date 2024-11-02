import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F
import asyncio

api = ""
logging.basicConfig(level=logging.INFO)
bot = Bot(token = api)
dp = Dispatcher()

@dp.message(Command('start'))
async def start(message: types.Message):
    print('Привет!\nЯ бот, помогающий твоему здоровью.')
    await message.answer('Привет!\nЯ бот, помогающий твоему здоровью.')

# Функция для обработки всех других сообщений
@dp.message(F.text)
async def all_messages(message: types.Message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer('Введите команду /start, чтобы начать общение.')

async def main():
    print("Бот весь в работе...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
