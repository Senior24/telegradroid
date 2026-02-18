from aiogram.filters import CommandStart
from aiogram.types import Message

from database.sql import db
from utils.gettext import _
from utils.modified_router import modified_router

router = modified_router("word_counter")

@router.message(CommandStart())
async def start(message: Message):
    lang = await db.lang(message.from_user.id)
    await message.answer(_("word_counter_start", lang))


@router.message()
async def count(message: Message):
    lang = await db.lang(message.from_user.id)
    words = len(message.text.split())
    symbols = len(message.text)
    await message.answer(_("counted_data", lang).format(words=words, symbols=symbols))
