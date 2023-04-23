import os
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters import Command
from aiogram import Bot, types
from aiogram.utils.exceptions import ChatNotFound

from app.loader import dp
from dotenv import load_dotenv
from app.bot.states import AnswerTo


load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

bot = Bot(BOT_TOKEN)

@dp.message_handler(Command("send"))
async def prepaid_answer(message: types.Message):
    if str(message.from_user.id) in str(ADMIN_ID):
        await message.answer("Напишите ID клиента, которому ответить")
        await AnswerTo.first()
    else:
        await message.answer("Эта опция только для админа")

@dp.message_handler(state=AnswerTo.id)
async def get_id(message: types.Message, state: FSMContext):
    mess = message.text
    await state.update_data(id=mess)
    await AnswerTo.next()
    await message.answer("Записал. Что ответим?")

@dp.message_handler(state=AnswerTo.message)
async def get_answer_and_send(message: types.Message, state: FSMContext):
    data = await state.get_data()
    id = data.get("id")
    mess = message.text
    await state.update_data(message=mess)
    try:
        await bot.send_message(id, f"Ответ от поддержки:\n{message['text']}")
        await state.finish()
        await message.answer("Отправлено!")
    except ChatNotFound:
        await message.answer("Отправка не удалась. Повторите позднее")
    await state.finish()
