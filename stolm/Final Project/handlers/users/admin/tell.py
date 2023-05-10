from asyncio import sleep
from aiogram import types, Bot
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from filters import IsPrivate
from loader import dp
from states import tell
from data.config import  admins_id, ConnectionToDB, BOT_TOKEN

bot = Bot(token=BOT_TOKEN)


@dp.message_handler(text='/tell', chat_id=admins_id)
async def get_id(message: types.Message):
    pass
