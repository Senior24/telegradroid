from aiogram import F
from aiogram.filters import CommandStart
from aiogram.types import Message

from database.sql import db
from utils.gettext import _
from utils.modified_router import modified_router

from .api.weather import get_weather

router = modified_router("weather")

@router.message(CommandStart())
async def start(message: Message):
    lang = await db.lang(message.from_user.id)

    await message.answer(_("weather_start", lang))

@router.message(F.text)
async def weather(message: Message):
    lang = await db.lang(message.from_user.id)

    try:
        weather = await get_weather(message.text, "imperial")

        await message.answer(_("weather_data", lang).format(
            temp=weather.main.temp,
            feels_like=weather.main.feels_like,
            temp_min=weather.main.temp_min,
            temp_max=weather.main.temp_max,
            pressure=weather.main.pressure,
            humidity=weather.main.humidity
        ))
    except:
        await message.answer(_("city_not_found", lang))
