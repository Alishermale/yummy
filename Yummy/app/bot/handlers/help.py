import os
from aiogram.types import CallbackQuery
from app.bot.keyboard.inline import basic_callback, home_buttons
from aiogram import types, Bot
from aiogram.dispatcher import FSMContext
from app.loader import dp
from dotenv import load_dotenv
from app.bot.states import SendMessage

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID").split()

bot = Bot(BOT_TOKEN)

@dp.callback_query_handler(basic_callback.filter(button_name='help'))
async def get_message(call: CallbackQuery):
    await call.message.answer("Напиши мне сообщение и я передам его в поддержку.\n Либо можешь вернуться на главную",
                              reply_markup=home_buttons)
    await SendMessage.first()

@dp.message_handler(state=SendMessage.message)
async def send(message: types.Message, state: FSMContext):
    mess = message.text
    await message.answer("Спасибо. Скоро мы обязательно ответим")
    await state.update_data(message=mess)
    for admin in ADMIN_ID:
        print(admin)
        await bot.send_message(admin, f"{message.from_user.full_name} "
                                       f"написал:\n{mess}\n\n ID для ответа: {message.from_user.id}")
    await state.finish()
