from aiogram.types import CallbackQuery
from app.bot.keyboard.inline import categories_bottons
from app.bot.keyboard.inline import basic_callback
from app.loader import dp


@dp.callback_query_handler(basic_callback.filter(button_name='looking_for_something'))
async def what_to_eat(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Выбери категории",
                              reply_markup=categories_bottons)
