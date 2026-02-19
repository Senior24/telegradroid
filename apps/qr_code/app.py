import cv2
import numpy as np

from aiogram import Bot, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from qreader import QReader

from database.sql import db
from utils.gettext import _
from utils.modified_router import modified_router

router = modified_router("qr_code")
qreader = QReader()

@router.message(CommandStart())
async def start(message: Message):
    lang = await db.lang(message.from_user.id)
    await message.answer(_("qr_code_start", lang))


@router.message(F.photo)
async def qr_code(message: Message, bot: Bot):
    photo = message.photo[-1]
    lang = await db.lang(message.from_user.id)

    file = await bot.get_file(photo.file_id)
    file_bytes = await bot.download_file(file.file_path)

    np_arr = np.frombuffer(file_bytes.getvalue(), np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    results = qreader.detect_and_decode(img)

    if not results:
        await message.answer(_("qr_code_not_found", lang))
        return

    response = "\n".join(result for result in results)
    await message.answer(response)
