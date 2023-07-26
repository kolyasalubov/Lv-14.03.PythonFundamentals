from aiogram.dispatcher.filters.state import StatesGroup, State


class tellto(StatesGroup):
    us_id = State()
    text = State()
