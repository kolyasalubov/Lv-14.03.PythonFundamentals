from aiogram import types, Bot
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import dp
from data.config import BOT_TOKEN, ConnectionToDB
from filters import IsPrivate
from utils.misc import rate_limit

bot = Bot(token=BOT_TOKEN)


@rate_limit(limit=10, key='/account')  # Middlewares
@dp.message_handler(IsPrivate(), text=['/account', '👤 Кабінет'])
async def info_about_user(message: types.Message):
    pass