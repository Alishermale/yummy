import logging
from logging.handlers import RotatingFileHandler

from aiogram import Dispatcher


async def on_startup(dp: Dispatcher):
    from app.bot.utils.startup_notify_admins import on_startup_notify
    await on_startup_notify(dp=dp)


# startup app
if __name__ == '__main__':
    from aiogram import executor
    from app.bot.handlers import dp

    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)

# logging
# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create a handler RotatingFileHandler
log_file = "app.log"
max_size = 100000
backup_count = 5
handler = RotatingFileHandler(filename=log_file, maxBytes=max_size, backupCount=backup_count)
handler.setLevel(logging.DEBUG)

# formatting messages
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
