from aiogram.filters import Filter
from aiogram.types import Message, Update

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

    async def __call__(self, update: Update) -> bool:
        user_data = next(
            (
                obj for obj in (
                update.message,
                update.edited_message,
                update.callback_query,
                update.inline_query,
                update.chat_member,
                update.my_chat_member,
                update.pre_checkout_query,
                update.shipping_query,
            )
                if obj is not None
            ),
            None,
        )

        thread_id = await db.app_thread_id(user_data.from_user.id, self.app)
        return thread_id == user_data.message_thread_id


