from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('menu', 'Меню бота'),
        types.BotCommand('help', 'Служба підтримки'),
        types.BotCommand('schedule', 'Розклад'),
        types.BotCommand('registration', 'Реєстрація'),
        types.BotCommand('account', 'Особистий кабінет')
        ])
