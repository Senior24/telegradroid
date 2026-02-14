from aiogram import BaseMiddleware
from aiogram.types import Update

from typing import Callable, Dict, Any, Awaitable

from datetime import datetime
from database.sql import db

class UpdateUser(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        update: Update,
        data: Dict[str, Any]
    ) -> Any:
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

        user_id = user_data.from_user.id
        first_name = user_data.from_user.first_name
        last_name = user_data.from_user.last_name
        username = user_data.from_user.username

        if user_id == data['bot'].id:
            return

        if not await db.check_user(user_id):
            await db.add_user(
                user_id=user_id,
                first_name=first_name,
                last_name=last_name,
                username=username,
                lang="en"
            )

        await db.update_user(user_id, first_name, last_name, username, datetime.now())

        return await handler(update, data)
