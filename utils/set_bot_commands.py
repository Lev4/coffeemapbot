from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("help", "Помощь"),
        types.BotCommand("show_coffee_near", "Показать на карте"),
        # types.BotCommand("callback", "Оставить контакт"),
    ])
