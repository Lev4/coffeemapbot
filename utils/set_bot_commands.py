from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("help", "Помощь"),
        types.BotCommand("coffee_on_map", "Показать на карте"),
        # types.BotCommand("callback", "Оставить контакт"),
    ])
