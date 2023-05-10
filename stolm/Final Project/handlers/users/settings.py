from aiogram import types, Bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import dp
from data.config import ConnectionToDB, BOT_TOKEN
from filters import IsPrivate
from utils.misc import rate_limit

bot = Bot(token=BOT_TOKEN)


@rate_limit(limit=5, key='/settings')
@dp.message_handler(IsPrivate(), text=['/settings', '⚙ Налаштування'])
async def settings(message: types.Message):
    """
    Function for settings in user's account
    """
    async with ConnectionToDB() as cursor:
        cursor.execute(f"""SELECT mail FROM validUser WHERE Telegram_id = {message.from_user.id}""")
        mail_status = cursor.fetchone()[0]

    if mail_status == "False":
        mail_in_button = "❌"
    else:
        mail_in_button = "✅"

    settings_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f"🔔 Сповіщення про початок пари: {mail_in_button}",
                                     callback_data=f"notif{mail_status}"),
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
    )

    await message.answer("<b>⚙ Доступні Вам налаштування:</b>", reply_markup=settings_button, parse_mode="html")


@dp.callback_query_handler(lambda call: call.data[0:5] == "notif")
async def change_notif(call: types.CallbackQuery):
    """
    Change status "mail" for user in DB
    """
    new_mail_status = ""
    text = ""
    if call.data[5:] == "True":
        new_mail_status += "False"
        text += "❌"
    elif call.data[5:] == "False":
        new_mail_status += "True"
        text += "✅"

    async with ConnectionToDB() as cursor:
        cursor.execute(f"""UPDATE validUser SET mail = "{new_mail_status}"
                       WHERE
                       Telegram_id = "{call.message.chat.id}" """)
        cursor.connection.commit()

    await call.message.answer(
        text=f"<b>🔔 Статус сповіщень про початок пари було змінено на: {text}\n"
             f"Для зміни інших налаштувань викличте повторно /settings</b>",
        parse_mode="html")
