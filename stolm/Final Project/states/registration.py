from aiogram.dispatcher.filters.state import StatesGroup, State


class reg(StatesGroup):
    first_name = State()
    last_name = State()
    patronymic = State()
    status = State()
    type = State()
    course = State()
    faculty = State()
    spec = State()
    band = State()
    subgroup = State()
