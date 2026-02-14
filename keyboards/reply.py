from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from utils.gettext import _

def main_menu(lang: str) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=_("store", lang)), KeyboardButton(text=_("settings", lang))]
    ], resize_keyboard=True)
