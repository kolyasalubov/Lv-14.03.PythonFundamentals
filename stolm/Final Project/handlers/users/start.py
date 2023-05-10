from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import dp
from utils.misc import rate_limit


@rate_limit(limit=10, key='/start')  # Middlewares
@dp.message_handler(text='/start')
async def command_start(message: types.Message):
    pass