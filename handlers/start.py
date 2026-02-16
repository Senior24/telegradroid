from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from database.sql import db
from keyboards.reply import main_menu
from utils.gettext import _


router = Router()

@router.message(CommandStart(), ~F.message_thread_id)
async def start(message: Message, state: FSMContext):
    await state.clear()
    lang = await db.lang(message.from_user.id)
    await message.answer(_("start", lang), reply_markup=main_menu(lang))
