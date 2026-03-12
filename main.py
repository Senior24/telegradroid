import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from data.config import BOT_TOKEN
from data.routers import routers_list
from database.pool import create_pool
from utils.db_setup import setup_tables
from utils.middlewares import UpdateUser

dp = Dispatcher()


async def main() -> None:
    default = DefaultBotProperties(parse_mode=ParseMode.HTML)
    bot = Bot(token=BOT_TOKEN, default=default)

    await create_pool()
    await setup_tables()

    dp.update.middleware(UpdateUser())
    dp.include_routers(*routers_list)

    print("Bot started")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())