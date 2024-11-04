import os
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
import logging
from crud_functions_14_5 import initiate_db, get_all_products, add_user, is_included
api = '7929017949:AAFbKr4_NnW-HeULUuyCxn5cDRTAKRkEuj0'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
initiate_db()
main_menu_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
main_menu_kb.add(types.KeyboardButton(text="Купить"), types.KeyboardButton(text="Регистрация"))
class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    logging.info("Пользователь активировал бот.")
    await message.answer("Здравствуйте!\n\nДобро пожаловать в магазин.\nВыберите, что хотите сделать:",
                         reply_markup=main_menu_kb)
@dp.message_handler(content_types=types.ContentType.TEXT)
async def handle_text(message: types.Message):
    if message.text == "Купить":
        await buy_products(message)
    elif message.text == "Регистрация":
        await sing_up(message)
async def sing_up(message):
    await RegistrationState.username.set()
    await message.answer("Введите имя пользователя (только латинский алфавит):")
@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if is_included(message.text):
        await message.answer("Пользователь существует, введите другое имя:")
    else:
        await state.update_data(username=message.text)
        await RegistrationState.email.set()
        await message.answer("Введите свой email:")
@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await RegistrationState.age.set()
    await message.answer("Введите свой возраст:")
@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    user_data = await state.get_data()
    username = user_data.get('username')
    email = user_data.get('email')
    age = message.text
    add_user(username, email, age)
    await message.answer("Вы успешно зарегистрировались!")
    await state.finish()
async def buy_products(message: types.Message):
    logging.info("Пользователь нажал 'Купить'. Отправляем продуктовый лист.")
    await get_buying_list(message)
async def get_buying_list(message: types.Message):
    pass
if __name__ == '__main__':
    logging.info("Бот в работе...")
    executor.start_polling(dp, skip_updates=True)