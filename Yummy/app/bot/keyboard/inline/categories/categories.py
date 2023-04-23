from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.bot.keyboard.inline.categories.callback_categories import categories_callback


categories_bottons = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Сладкое",
            callback_data=categories_callback.new(button_name='sweet')
        )
    ],
    [
        InlineKeyboardButton(
            text="Острое",
            callback_data=categories_callback.new(button_name='spicy')
        )
    ]
])
