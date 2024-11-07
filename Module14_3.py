import os

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import logging

api = '7929017949:AAFbKr4_NnW-HeULUuyCxn5cDRTAKRkEuj0'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

main_menu_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
main_menu_kb.add(types.KeyboardButton(text="Купить"))

catalogue_kb = types.InlineKeyboardMarkup(inline_keyboard=[
    [types.InlineKeyboardButton(text='Product1', callback_data='product_buying')],
    [types.InlineKeyboardButton(text='Product2', callback_data='product_buying')],
    [types.InlineKeyboardButton(text='Product3', callback_data='product_buying')],
    [types.InlineKeyboardButton(text='Product4', callback_data='product_buying')]
])

products_info = {
    'Product1': ('Описание продукта 1', 1, 'Sauce/Чипотл.png'),
    'Product2': ('Описание продукта 2', 2, 'Sauce/Цитрус.png'),
    'Product3': ('Описание продукта 3', 3, 'Sauce/Бафало Блад.png'),
    'Product4': ('Описание продукта 4', 4, 'Sauce/Гарлик.png')
}

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    logging.info("A user started the bot.")
    await message.answer("Здравствуйте! Добро пожаловать в магазин. Выберите, что хотите сделать:",
                         reply_markup=main_menu_kb)


@dp.message_handler(text="Купить")
async def buy_products(message):
    logging.info("User pressed 'Купить'. Sending product list.")
    await get_buying_list(message)


async def get_buying_list(message):
    for product_name, (description, number, image_path) in products_info.items():
        price = number * 100
        await message.answer(f'Название: {product_name} | Описание: {description} | Цена: {price}')
        if os.path.exists(image_path):
            with open(image_path, 'rb') as img:
                await message.answer_photo(photo=img)
    logging.info("Product list sent. Asking for product selection.")

    await message.answer("Выберите продукт для покупки:", reply_markup=catalogue_kb)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    logging.info(f"Received callback with data: {call.data}")

    product_name = {
        'product1': 'Product1',
        'product2': 'Product2',
        'product3': 'Product3',
        'product4': 'Product4'
    }[call.data]
    logging.info(f"User selected {product_name}. Sending confirmation message.")
    await call.message.answer(f'Вы успешно приобрели продукт!')

if __name__ == '__main__':
    logging.info("Starting the bot...")
    executor.start_polling(dp, skip_updates=True)
