from aiogram.dispatcher.filters.state import StatesGroup, State


class SendMessage(StatesGroup):
    message = State()
    deny = State()
