from aiogram.dispatcher.filters.state import StatesGroup, State


class bot_mailing(StatesGroup):
    text = State()
    state = State()
    photo = State()
    filter_course = State()
    filter_fac = State()
    filter_spec = State()
    filter_band = State()
