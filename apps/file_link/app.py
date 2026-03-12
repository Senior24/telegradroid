from aiogram import F
from aiogram.types import Message

from utils.modified_router import modified_router

from .code_generator import generate
from .db import Database

router = modified_router("file_link")
db = Database()


@router.message(F.text)
async def file_link(message: Message):
    file_id = await db.get_data("file_id", message.text, "code")

    if not file_id:
        return

    content_type = await db.get_data("content_type", file_id, "file_id")

    if content_type == "photo":
        await message.answer_photo(file_id)
    else:
        await message.answer_document(file_id)

@router.message(F.document | F.video | F.photo)
async def video(message: Message):
    if message.document:
        file_id = message.document.file_id
        content_type = "file"
    elif message.video:
        file_id = message.video.file_id
        content_type = "video"
    elif message.photo:
        file_id = message.photo[-1].file_id
        content_type = "photo"

    code = await db.get_data("code", file_id, "file_id")

    if not code:
        code = generate()
        if await db.get_data("code", code, "code"):
            await message.answer("pls try again")
            return

        await db.add_record(file_id, content_type, code)

    await message.answer(f"<code>{code}</code>")
