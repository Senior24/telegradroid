from aiogram import F
from aiogram.types import Message

from utils.modified_router import modified_router

router = modified_router("qr_code")

@router.message(F.photo)
@router.message(F.document)
async def qr_code(message: Message):
    await message.answer("QR code")

@router.message(F.text)
async def text(message: Message):
    await message.answer("Text")
