from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from .gettext import _

def content_list(lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text=_("images", lang), callback_data="images"),
        InlineKeyboardButton(text=_("videos", lang), callback_data="videos"),
        InlineKeyboardButton(text=_("news", lang), callback_data="news"),
    ]])
