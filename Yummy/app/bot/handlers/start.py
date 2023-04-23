from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from app.bot.keyboard.inline import basic_bottons, home_callback
from app.loader import dp


@dp.message_handler(Command("start"))
async def command_start(message: types.Message):
    await message.answer(f"Привет {message.from_user.first_name}! Я бот магазина Yummy. Что вы хотите заказать?",
                         reply_markup=basic_bottons)


@dp.callback_query_handler(home_callback.filter(button_name='home'))
async def to_home(call: CallbackQuery):
    await call.message.answer(
        f"Привет {call.message.from_user.first_name}! Я бот магазина Yummy. Что вы хотите заказать?",
        reply_markup=basic_bottons)
