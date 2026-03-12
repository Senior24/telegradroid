from aiogram import BaseMiddleware
from aiogram.enums import ChatType
from aiogram.types import TelegramObject

from typing import Callable, Dict, Any, Awaitable

from datetime import datetime
from database.sql import db

class UpdateUser(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        event_chat = data.get('event_chat')
        if not event_chat or event_chat.type != ChatType.PRIVATE:
            return await handler(event, data)

        user = data['event_from_user']

        if user.id == data['bot'].id:
            return

        if not await db.check_user(user.id):
            await db.add_user(
                user_id=user.id,
                first_name=user.first_name,
                last_name=user.last_name,
                username=user.username,
                lang="en"
            )

        await db.update_user(user.id, user.first_name, user.last_name, user.username, datetime.now())

        return await handler(event, data)
