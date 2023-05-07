from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from filters import IsPrivate
from loader import dp
from states import reg
from data.config import ConnectionToDB
from utils.misc import rate_limit


@rate_limit(limit=15, key='/registration')  # Middlewares
@dp.message_handler(IsPrivate(), text=["/registration", "🔓 Зареєструватися"])
async def command_start(message: types.Message):
    pass
