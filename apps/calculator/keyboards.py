from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def default() -> InlineKeyboardMarkup:
    keyboard = [
        "1", "2", "3",
        "4", "5", "6",
        "7", "8", "9",
        "0", "<", "=",
    ]

    builder = InlineKeyboardBuilder()

    for key in keyboard:
        builder.button(text=key, callback_data=key)

    builder.adjust(3)
    return builder.as_markup()
