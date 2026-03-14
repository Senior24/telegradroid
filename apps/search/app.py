from aiogram import F
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from pyexpat.errors import messages

from database.sql import db
from utils.modified_router import modified_router

from .api.search import get_websites
from .keyboards import content_list

router = modified_router("search")

@router.message(F.text)
async def search_web(message: Message):
    data = await get_websites(message.text)
    lang = await db.lang(message.from_user.id)
    results = ""
    for number, website in enumerate(data.web.results, start=1):
        results += f"<a href='{website.url}'>{number}. {website.title}</a>\n"

    await message.answer(results, disable_web_page_preview=True)


@router.callback_query()
async def search_content(callback: CallbackQuery):
    pass
