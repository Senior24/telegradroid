from aiogram import F
from aiogram.filters import CommandStart
from aiogram.types import Message

from database.sql import db
from utils.modified_router import modified_router

from .gettext import _

router = modified_router("handwriting")

@router.message(CommandStart())
async def start(message: Message):
    lang = await db.lang(message.from_user.id)
    await message.answer(_("start", lang))


@router.message(F.text)
async def text(message: Message):
    lang = await db.lang(message.from_user.id)
    processed_text = message.text.replace(" ", "+")

    try:
        await message.answer_photo("https://apis.xditya.me/write?text="+processed_text)
    except:
        await message.answer(_("invalid_symbols", lang))
