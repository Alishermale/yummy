import logging
from aiogram import Dispatcher
from ..data.config import ADMIN_ID


async def on_startup_notify(dp: Dispatcher):
    try:
        for admin in ADMIN_ID:
            await dp.bot.send_message(admin, "Бот Запущен")

    except Exception as err:
        logging.exception(err)
