from asyncio import sleep
from aiogram import types, Bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from loader import dp
from datetime import datetime, date, time
import aioschedule
import json
import asyncio
from data.config import BOT_TOKEN, ConnectionToDB
from parse import collect_schedule
from utils.misc import rate_limit
from states.registration import reg
from aiogram.dispatcher import FSMContext


bot = Bot(token=BOT_TOKEN)

weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

lessons = {
    1: ["08:00", "09:20"],
    2: ["09:30", "10:50"],
    3: ["11:10", "12:30"],
    4: ["13:00", "14:20"],
    5: ["14:40", "16:00"],
    6: ["16:10", "17:30"],
    7: ["17:30", "19:00"]
}


async def change_week():
    """
    Function to change week number
    """
    with open("week.json", "r", encoding="utf8") as week:
        data = json.load(week)
        if data["week"] == 1:
            data["week"] = 2
        else:
            data["week"] = 1
    with open("week.json", "w", encoding="utf8") as week:
        json.dump(data, week)


async def change_day():
    """
    Function to change number of day
    """
    date_now = datetime.today()
    with open("week.json", "r", encoding="utf8") as day:
        data = json.load(day)
        data["day"] = (date_now.weekday() + 1) % 7
    with open("week.json", "w", encoding="utf8") as day:
        json.dump(data, day)


async def calling():
    """
    Function to parse our schedule from the site
    and to change week number
    """
    aioschedule.every().monday.at("00:01").do(change_week)
    aioschedule.every(1).week.do(collect_schedule)
    aioschedule.every().day.at("00:00").do(change_day)

    aioschedule.every().day.at("07:55").do(mailing_lesson, 1)
    aioschedule.every().day.at("09:25").do(mailing_lesson, 2)
    aioschedule.every().day.at("11:05").do(mailing_lesson, 3)
    aioschedule.every().day.at("12:55").do(mailing_lesson, 4)
    aioschedule.every().day.at("14:35").do(mailing_lesson, 5)
    aioschedule.every().day.at("16:05").do(mailing_lesson, 6)
    aioschedule.every().day.at("17:25").do(mailing_lesson, 7)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def filter_choice(results, user_id, WeekNum=0, WeekDay=0, message_id=None):
    """
    Function for sending the schedule for the selected day and week number
    """
    async with ConnectionToDB() as cursor:
        cursor.execute(f"""SELECT band, subgroup FROM validUser WHERE Telegram_id LIKE "{user_id}" """)
        result = cursor.fetchone()
        group, subgroup = result

    if WeekNum == 0:
        with open("week.json", "r", encoding="utf8") as f:
            data = json.load(f)
            WeekNum = "week" + str(data["week"])
            WeekDay = int(data["day"])
    filtered_results = [result for result in results
                        if(result["SubGroup"] == 0 or result["SubGroup"] == int(subgroup)) and
                        ((result["Week"] == 0 or result["Week"] == int(WeekNum[4]))
                         and (result["WeekDay"] == WeekDay))]

    text = f"🎓<b>Ваша група: </b>{group}\n\n"

    if filtered_results:
        text += "\n".join([
                f"==============================\n\n"
                f"<b>📚 {result['Title']}</b>\n<b>📒 Тип роботи: </b>{result['Type']}\n"\
                f"<b>📎 Посилання на курс: </b> {result['URL']}\n" if result['Room'] == 'ATutor' else
                f"==============================\n\n"
                f"<b>{result['Title']}</b>\n<b>📒 Тип роботи: </b>{result['Type']}\n"\
                f"<b>🏬 Кабінет:</b> {result['Room']}\n" for result in filtered_results
        ])

    else:
        text += "<b>🎉 Сьогодні вихідний! Можеш трохи відпочити 🙂</b>"
    markup = InlineKeyboardMarkup(
                                    inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text="Понеділок ✅" if WeekDay == 1 else "Понеділок",
                                                                   callback_data=f"{WeekNum}monday")],
                                          [
                                              InlineKeyboardButton(text="Вівторок ✅" if WeekDay == 2 else "Вівторок",
                                                                   callback_data=f"{WeekNum}tuesday")],
                                          [
                                              InlineKeyboardButton(text="Середа ✅" if WeekDay == 3 else "Середа",
                                                                   callback_data=f"{WeekNum}wednesday")],
                                          [
                                              InlineKeyboardButton(text="Четвер ✅" if WeekDay == 4 else "Четвер",
                                                                   callback_data=f"{WeekNum}thursday")],
                                          [
                                              InlineKeyboardButton(text="П'ятниця ✅" if WeekDay == 5 else "П'ятниця",
                                                                   callback_data=f"{WeekNum}friday"),
                                          ],

                                          [
                                              InlineKeyboardButton(text="1 тиждень ✅" if WeekNum == "week1"
                                                                   else "1 тиждень", callback_data=f"week1{weekdays[WeekDay-1]}"),
                                              InlineKeyboardButton(text="2 тиждень ✅" if WeekNum == "week2"
                                                                   else "2 тиждень", callback_data=f"week2{weekdays[WeekDay-1]}"),
                                          ]
                                      ]
        )
    if message_id:
        await bot.edit_message_text(chat_id=user_id, message_id=message_id, text=text,
                                    reply_markup=markup, parse_mode="html")
    else:
        message = await bot.send_message(chat_id=user_id, text=text, reply_markup=markup, parse_mode="html")
        message_id = message.message_id
    return message_id


@dp.callback_query_handler(lambda call: call.data[5:] in weekdays or call.data[0:4] == "week")
async def handle_weekday_callback(call: types.CallbackQuery):
    """
    Using /schedule for other days
    """
    async with ConnectionToDB() as cursor:
        cursor.execute(f"""SELECT faculty, band FROM validUser WHERE Telegram_id LIKE "{call.message.chat.id}" """)
        user = cursor.fetchone()
        user_id = call.message.chat.id
    # current_weekday = today
    with open("week.json", "r", encoding="utf8") as f:
        current_week = json.load(f)["week"]
    if call.data[5:] in weekdays:
        current_weekday = call.data[5:]
    if call.data[0:4] == "week":
        current_week = call.data[0:5]
    if user:
        faculty = user[0][-4:-1]
        group = user[1]
        with open("info.json", "r", encoding="utf8") as file:
            our_schedule = json.load(file)
            result = our_schedule[faculty][group]
            message_id = call.message.message_id
            await filter_choice(result, user_id, WeekNum=current_week,
                                WeekDay=weekdays.index(call.data[5:])+1, message_id=message_id)


async def mailing_lesson(lesson_number):
    """
    Sends 5 minutes before the start of the message about the couple
    """
    with open("week.json", "r", encoding="utf8") as f:
        week_day = json.load(f)
    today = week_day["day"]
    week = week_day["week"]
    with open("info.json", "r", encoding="utf8") as f:
        data = json.load(f)
        async with ConnectionToDB() as cursor:
            cursor.execute(f"""SELECT Telegram_id, faculty, band, subgroup FROM validUser WHERE mail = 'True' """)
            users = cursor.fetchall()
            for user in users:
                try:
                    current_lesson = list(filter(
                        lambda x: x['Number'] == lesson_number and (x['WeekDay'] == today)
                        and (x['Week'] == 0 or x['Week'] == week)
                        and (x['SubGroup'] == 0 or x['SubGroup'] == user[3]),
                        data[str(user[1][-4:-1])][user[2]]))
                    if current_lesson:
                        current_lesson = current_lesson[0]
                        if current_lesson["Room"] == "ATutor":
                            type_of_lesson = f"\n<b>📎 Посилання на курс: </b> {current_lesson['URL']}"
                        else:
                            type_of_lesson = f"\n <b>🏬 Кабінет: </b> {current_lesson['Room']}"
                        await bot.send_message(chat_id=user[0], text=f"<b>🔔 В тебе за 5 хвилин розпочнеться:</b> {current_lesson['Title']}"
                                                                     f" {type_of_lesson}",
                                                                     parse_mode="html")
                        await sleep(0.15)
                except Exception:
                    pass


@dp.message_handler(state=reg.subgroup)
async def update_subgroup(message: types.Message, state: FSMContext):
    """
    Function to set a person's subgroup in our database if it is not available.
    If the subgroup in the table is already set,
    the function will not be called.
    """
    answer = message.text
    if answer == "1" or answer == "2":
        await state.update_data(subgroup=answer)
        async with ConnectionToDB() as cursor:
            sql = """UPDATE validUser SET subgroup = ?
                    WHERE 
                    Telegram_id LIKE ? """
            values = (answer, message.from_user.id)
            cursor.execute(sql, values)
            cursor.connection.commit()
            await state.finish()
            await message.answer(
                "<b>🎉 Дякуємо! Вашу підгрупу встановлено. Відтепер можете користуватися розкладом!</b>",
                parse_mode="html")
    else:
        await message.answer("<b>❌ Обраної Вами підгрупи не знайдено! Спробуйте, будь ласка, ще раз! </b>",
                             parse_mode="html")


@dp.message_handler(text="❌ Скасувати вибір підгрупи", state=[reg.subgroup])
async def quit(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("<b>❌ Підтвердження вибору скасовано!</b>", parse_mode='html')


@rate_limit(limit=5, key='/schedule')  # Middlewares
@dp.message_handler(text=['/schedule', '🗓 Розклад'])
async def command_schedule(message: types.Message):
    """
    Our main message handler for command /schedule
    """
    async with ConnectionToDB() as cursor:
        cursor.execute(f"""SELECT faculty, band FROM validUser WHERE Telegram_id LIKE "{message.from_user.id}" """)
        user = cursor.fetchone()
        user_id = message.from_user.id
    if user:
        async with ConnectionToDB() as cursor:
            cursor.execute(f"""SELECT subgroup FROM validUser WHERE Telegram_id LIKE "{message.from_user.id}" """)
            subgroup = cursor.fetchone()
        if subgroup is None or not subgroup[0]:
            subgroup_button = ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(text="1"),
                        KeyboardButton(text="2")
                    ],
                    [
                        KeyboardButton(text="❌ Скасувати вибір підгрупи")
                    ]
                ],
                resize_keyboard=True,
                one_time_keyboard=True
            )
            await message.answer("<b>❗ Оберіть для початку Вашу підгрупу:</b>",
                                 reply_markup=subgroup_button, parse_mode="html")
            await reg.subgroup.set()
        else:
            faculty = user[0][-4:-1]
            group = user[1]
            with open("info.json", "r", encoding="utf8") as file:
                our_schedule = json.load(file)
                result = our_schedule[faculty][group]
                await filter_choice(result, user_id)
    else:
        await message.answer('<b>Вас не знайдено у базі данних (або розклад вашої групи у розробці!)</b>\n'
                             'Використовуйте команду /registration - для реєстрації', parse_mode='html')
