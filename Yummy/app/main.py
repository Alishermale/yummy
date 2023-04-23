# startup app and notify admins
# notify admins
async def on_startup(dp):
    from app.bot.utils.startup_notify_admins import on_startup_notify
    await on_startup_notify(dp)


# startup app
if __name__ == '__main__':
    from aiogram import executor
    from app.bot.handlers import dp

    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
