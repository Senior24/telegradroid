from aiogram import Router, Bot, F
from aiogram.types import Message, CallbackQuery

from database.sql import db
from keyboards.inline import unattached_apps
from utils.custom_emoji import get_emoji_id
from utils.filters import Text
from utils.gettext import _

router = Router()

@router.message(Text("store"))
async def store(message: Message):
    user_id = message.from_user.id
    lang = await db.lang(user_id)
    await message.answer(_("store", lang), reply_markup=await unattached_apps(user_id))


@router.callback_query(F.data.startswith("app"))
async def app_handler(callback: CallbackQuery, bot: Bot):
    query = callback.data.split("_")
    user_id = callback.from_user.id
    lang = await db.lang(user_id)
    app = _(query[2], lang).split()

    if query[1] == "add":
        await bot.create_forum_topic(user_id, app[1],
                                     icon_custom_emoji_id=get_emoji_id(app[0]))
