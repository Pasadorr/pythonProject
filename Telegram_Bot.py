import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F
import asyncio

api = ""
logging.basicConfig(level=logging.INFO)

# Создание объектов бота и диспетчера
bot = Bot(token=api)
dp = Dispatcher()

# Функция для обработки команды /start
@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer('Привет!\nЯ бот, помогающий твоему здоровью.')

# Функция для обработки всех других сообщений
@dp.message(F.text)
async def all_messages(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.')

# Основная асинхронная функция для запуска бота
async def main():
    print("Bot is working...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
