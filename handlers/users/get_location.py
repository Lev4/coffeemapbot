from aiogram import types
from aiogram.dispatcher.filters import Command
from keyboards.default import location_button
from utils.misc.calc_distance import choose_shortest
from loader import dp, bot


@dp.message_handler(Command("show_coffee_near"))
async def share_number(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}.\n"
                         f"Для того, чтобы показать ближайшие кофейни отправь свою локацию "
                         f"нажав на кнопку ниже!", reply_markup=location_button.keyboard)


@dp.message_handler(content_types=types.ContentType.LOCATION)
async def get_contact(message: types.Message):
    location = message.location
    latitude = location.latitude
    longitude = location.longitude
    closest_shops = choose_shortest(location)

    text = "\n\n".join([f"{shop_name}. <a href='{url}'>Google</a>\n Расстояние до кофейни: {distance:.1f} км."
                        for shop_name, distance, url, shop_location in closest_shops])

    await message.answer(f"Спасибо. Нашлось  {len(closest_shops)}. \n"
                         
                         f"{text}", disable_web_page_preview=True)

    for shop_name, distance, url, shop_location in closest_shops:
        await message.answer_location(latitude=shop_location["lat"],
                                      longitude=shop_location["lon"])
