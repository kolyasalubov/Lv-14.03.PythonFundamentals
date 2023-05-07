from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import dp
from data.config import ConnectionToDB
from filters import IsPrivate
from utils.misc import rate_limit
from datetime import datetime


@rate_limit(limit=5, key='/menu')
@dp.message_handler(IsPrivate(), Command('menu'))
async def command_menu(message: types.Message):
    pass