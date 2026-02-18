from aiogram import F
from aiogram.types import Message

from utils.modified_router import modified_router

from .api.weather import get_weather

router = modified_router("weather")

@router.message(F.text)
async def weather(message: Message):
    pass