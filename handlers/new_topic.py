from aiogram import Router, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message

from utils.filters import NewThread
from database.sql import db
from utils.gettext import _

router = Router()

@router.message(CommandStart(), NewThread())
async def new_topic(message: Message, bot: Bot):
    user_id = message.from_user.id
    thread_id = message.message_thread_id
    lang = await db.lang(user_id)
    await message.answer(_("new_topic", lang))

    pending_app = await db.pending_app(user_id)

    if pending_app:
        await db.add_app(user_id, pending_app, thread_id)
    else:
        await bot.delete_message(user_id, thread_id)