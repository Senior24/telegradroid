from aiogram import F
from aiogram.filters import CommandStart
from aiogram.types import Message

from database.sql import db
from utils.modified_router import modified_router

from .gettext import _

router = modified_router("word_counter")

@router.message(CommandStart())
async def start(message: Message):
    lang = await db.lang(message.from_user.id)
    await message.answer(_("start", lang))


@router.message(F.text)
async def count(message: Message):
    lang = await db.lang(message.from_user.id)
    words = len(message.text.split())
    symbols = len(message.text)
    await message.answer(_("counted_data", lang).format(words=words, symbols=symbols))
