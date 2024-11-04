import os
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import executor
import logging
from crud_functions import initiate_db, get_all_products

api = ''
logging.basicConfig(level=logging.INFO)
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
initiate_db()
main_menu_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
main_menu_kb.add(types.KeyboardButton(text="Купить"))

@dp.message_handler(commands=["start"])
async def start(message):
    logging.info("Пользователь активировал бот.")
    await message.answer("Здравствуйте! Добро пожаловать в магазин. Выберите, что хотите сделать:",
                         reply_markup=main_menu_kb)

products_info = ['Sauce/Чипотл.png',
                 'Sauce/Цитрус.png',
                 'Sauce/Бафало Блад.png',
                 'Sauce/Гарлик.png']
@dp.message_handler(content_types=types.ContentType.TEXT)
async def handle_text(message):
    if message.text == "Купить":
        await buy_products(message)
async def buy_products(message: types.Message):
    logging.info("Пользователь нажал 'Купить'. Отправляем продуктовый лист.")
    await get_buying_list(message)
async def get_buying_list(message):
    products = get_all_products()

    if not products:
        await message.answer("Нет доступных продуктов.")
        return
    for idx, product in enumerate(products):
        if idx < len(products_info):
            image_url = products_info[idx]  # Получаем путь к изображению

            if os.path.exists(image_url):
                product_id, title, description, price = product
                with open(image_url, 'rb') as photo:
                    await message.answer_photo(photo=photo,
                                               caption=f'Название: {title} | Описание: {description} | Цена: {price}')

    logging.info("Список отправлен. Запрашиваем выбор.")
if __name__ == '__main__':
    logging.info("Бот в работе...")
    executor.start_polling(dp, skip_updates=True)

