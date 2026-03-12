from aiogram import Router
from aiogram.types import Message

router = Router()

@router.channel_post()
async def post(message: Message):
    pass