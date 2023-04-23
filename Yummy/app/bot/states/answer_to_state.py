from aiogram.dispatcher.filters.state import StatesGroup, State


class AnswerTo(StatesGroup):
    id = State()
    message = State()
