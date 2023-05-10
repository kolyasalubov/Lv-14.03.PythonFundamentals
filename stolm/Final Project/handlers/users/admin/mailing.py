from asyncio import sleep
from aiogram import types, Bot
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from filters import IsPrivate
from loader import dp
from states import bot_mailing
from data.config import BOT_TOKEN, ConnectionToDB


bot = Bot(token=BOT_TOKEN)


@dp.message_handler(IsPrivate(), text=["/post", "📨 Зробити оголошення"])
def post():
    pass