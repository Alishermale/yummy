from aiogram.types import CallbackQuery
from app.bot.keyboard.inline import categories_callback
from app.loader import dp


@dp.callback_query_handler(categories_callback.filter(button_name='spicy'))
async def spicy(call: CallbackQuery):
    await call.message.answer("Сгорит")
