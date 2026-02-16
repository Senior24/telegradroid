from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from utils.filters import App
from utils.modified_router import modified_router

from .keyboards import default

router = modified_router("calculator")


@router.message(CommandStart())
async def start(message: Message):
    await message.answer("0", reply_markup=default())


@router.callback_query()
async def process(callback: CallbackQuery):
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    operations = ["+", "-", "*", "/"]
    key = callback.data
    text = callback.message.text

    if key in digits + operations:
        await callback.message.edit_text(text + key, reply_markup=default())
    if key == "<":
        await callback.message.edit_text(text[:-1], reply_markup=default())
    if key == "=":
        await callback.message.edit_text(eval(text), reply_markup=default())
