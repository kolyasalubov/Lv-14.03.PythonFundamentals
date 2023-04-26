from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('Головне меню')
subscribe_time = KeyboardButton('Підписка час')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(subscribe_time)
