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
    await message.answer(_("choose_app_to_add", lang), reply_markup=await unattached_apps(user_id))


@router.callback_query(F.data.startswith("app_add"))
async def app_handler(callback: CallbackQuery, bot: Bot):
    query = callback.data.split("_")
    user_id = callback.from_user.id
    lang = await db.lang(user_id)
    user_apps = await db.apps(user_id)
    app = "_".join(query[2:])
    app_name = _(app, lang).split()

    if query[2] not in user_apps:
        new_thread = await bot.create_forum_topic(user_id, " ".join(app_name[1:]),
                                                  icon_custom_emoji_id=get_emoji_id(app_name[0]))
        await db.add_app(user_id, query[2], new_thread.message_thread_id)
        await callback.answer(_("app_attached_to_chat", lang), show_alert=True)
    else:
        await callback.answer(_("app_added_already", lang))

    await callback.message.edit_reply_markup(reply_markup=await unattached_apps(user_id))
