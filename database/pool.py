import os

from contextlib import suppress

from database.postgresql import PostgreSQL
from database import sql

db = PostgreSQL()

async def create_pool():
    await db.create()
    pool = db.pool
    sql.db.pool = pool

    for app in os.listdir('apps'):
        with suppress(AttributeError):
            module = __import__(f"apps.{app}.app", fromlist=["db"])
            module.db.pool = pool
