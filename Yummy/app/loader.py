# download all app parameters for work
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from app.db.sqlite import Database
from app.bot.data import config


bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

storage = MemoryStorage()
db = Database()
dp = Dispatcher(bot, storage=storage)

__all__ = ["bot", "storage", "dp", "db"]
