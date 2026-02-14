from aiogram import Router
from aiogram.types import Message

from utils.filters import NewThread
from database.sql import db
from keyboards.inline import unattached_apps
from utils.gettext import _

router = Router()

@router.message(NewThread())
async def new_topic(message: Message):
    user_id = message.from_user.id
    lang = await db.lang(user_id)
    await message.answer(_("new_topic", lang), reply_markup=await unattached_apps(user_id))
