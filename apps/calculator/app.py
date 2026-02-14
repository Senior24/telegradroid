from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from utils.filters import App

from .keyboards import default

router = Router()
router.message.filter(App("calculator"))
router.callback_query.filter(App("calculator"))


@router.message(CommandStart())
async def start(message: Message):
    await message.answer("0", reply_markup=default())
