import os

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from database.sql import db
from utils.gettext import locales, _

def lang_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for lang in locales.keys():
        builder.button(text=_("name", lang), callback_data=f"lang_{lang}")

    builder.adjust(2)
    return builder.as_markup()

def settings(lang: str):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=_("change_lang", lang), callback_data=f"change_lang")]
    ])

async def store_apps(user_id: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    user_apps = await db.apps(user_id)
    lang = await db.lang(user_id)

    for app in os.listdir("apps"):
        if not app.startswith(("_", ".")) and app not in user_apps:
            builder.button(text=_(app, lang), callback_data=f"app:add:{app}")

    builder.button(text=_("remove_apps", lang), callback_data="app:remove")

    builder.adjust(2)
    return builder.as_markup()

async def remove_apps(user_id: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    user_apps = await db.apps(user_id)
    lang = await db.lang(user_id)

    for app in os.listdir("apps"):
        if not app.startswith(("_", ".")) and app in user_apps:
            builder.button(text=_(app, lang), callback_data=f"app:remove:{app}")

    builder.button(text=_("back", lang), callback_data="app:add")

    builder.adjust(2)
    return builder.as_markup()
