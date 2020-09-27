from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default import location_button
from loader import dp


@dp.message_handler(CommandStart())
async def share_locatation_on_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}!\n"
                         f"Чтобы посмотреть ближайшие кофейни, отправь свою локацию, "
                         f"нажав на кнопку ниже!", reply_markup=location_button.keyboard)
