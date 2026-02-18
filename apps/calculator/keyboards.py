from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def default() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    buttons = [
        "1", "2", "3", "+",
        "4", "5", "6", "-",
        "7", "8", "9", "*",
        "0", "=", "/", "<"
    ]

    for button in buttons:
        builder.button(text=button, callback_data=button)

    builder.adjust(4)

    return builder.as_markup()

