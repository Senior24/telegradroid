from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("panel", prefix="/!"))
async def panel(message: Message):
    await message.answer("Welcome to panel")
