from aiogram.dispatcher.filters.state import StatesGroup, State


class helping(StatesGroup):
    who = State()
    item = State()
    user_state = State()