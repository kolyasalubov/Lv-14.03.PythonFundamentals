from aiogram import types, Bot
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from loader import dp
from data.config import BOT_TOKEN, ConnectionToDB
from filters import IsPrivate
from states import helping
from utils.misc import rate_limit


bot = Bot(token=BOT_TOKEN)


@rate_limit(limit=10, key='/help')  # Middlewares
@dp.message_handler(IsPrivate(), text=['/help', '❓ Поставити запитання'])
async def get_question(message: types.Message):
    pass