from aiogram.filters import Filter
from aiogram.types import TelegramObject, Message

from database.sql import db
from utils.gettext import _


class NewThread(Filter):
    async def __call__(self, message: Message) -> bool:
        apps = await db.apps(message.from_user.id)
        thread_id = message.message_thread_id
        if thread_id and thread_id not in apps.values():
            return True

        return False


class Text(Filter):
    def __init__(self, key: str) -> None:
        self.key = key

    async def __call__(self, message: Message) -> bool:
        lang = await db.lang(message.from_user.id)
        return message.text == _(self.key, lang)


class App(Filter):
    def __init__(self, app: str) -> None:
        self.app = app

    async def __call__(self, event: TelegramObject, event_from_user) -> bool:
        app_thread_id = await db.app_thread_id(event_from_user.id, self.app)

        if isinstance(event, Message):
            thread_id = event.message_thread_id
        else:
            thread_id = event.message.message_thread_id

        if thread_id == app_thread_id:
            return True
        return False
