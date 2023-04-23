from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.bot.keyboard.inline.home.callback_home import home_callback


home_buttons = InlineKeyboardMarkup(inline_keyboard=[
   [
       InlineKeyboardButton(
        text="Главная.",
        callback_data=home_callback.new(button_name="home")
    )
   ]
])
