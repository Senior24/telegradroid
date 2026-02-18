from aiogram import F
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from contextlib import suppress

from database.sql import db
from utils.gettext import _
from utils.modified_router import modified_router

from .keyboards import default

router = modified_router("calculator")

@router.message(CommandStart())
async def calculator(message: Message):
    await message.answer("0", reply_markup=default())


@router.message(F.text)
async def calculate(message: Message):
    try:
        await message.answer(str(eval(message.text)))
    except:
        lang = await db.lang(message.from_user.id)
        await message.answer(_("invalid_expression", lang))


@router.callback_query(F.data)
async def calculator_buttons(callback: CallbackQuery):
    button = callback.data
    message_text = callback.message.text
    operators_list = ["+", "-", "*", "/"]

    if button not in operators_list + ["=", "<"]:
        if message_text == "0":
            message = button[:]
        else:
            message = message_text + button

    elif button in operators_list:
        if message_text[-1] in operators_list:
            message = message_text[:-1] + button
        else:
            message = message_text + button

    elif button == "<":
        if len(message_text) == 1:
            message = "0"
        else:
            message = callback.message.text[:-1]

    elif button == "=":
        try:
            message = str(eval(callback.message.text))
        except ZeroDivisionError:
            message = "-"
        except:
            message = "0"

    with suppress(TelegramBadRequest):
        await callback.message.edit_text(message,
                                         reply_markup=default())
    await callback.answer()
