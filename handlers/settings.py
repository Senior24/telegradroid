from aiogram import Router
from aiogram.types import Message

from database.sql import db
from utils.filters import Text
from utils.gettext import _

router = Router()

@router.message(Text("settings"))
async def settings(message: Message):
    user_id = message.from_user.id
    lang = await db.lang(user_id)

    await message.answer("Currently there is only one language available. "
                         "Therefore, there no options for settings")