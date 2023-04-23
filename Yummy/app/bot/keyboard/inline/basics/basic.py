from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.bot.keyboard.inline.basics.callback_basic import basic_callback


basic_bottons = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Хочу что-то выбрать",
            callback_data=basic_callback.new(button_name='looking_for_something')
        )
    ],
    [
        InlineKeyboardButton(
            text="О нас.",
            callback_data=basic_callback.new(button_name='about')
        )
    ],
    [
        InlineKeyboardButton(
            text="Поддержка",
            callback_data=basic_callback.new(button_name='help')
        )
    ]
])
