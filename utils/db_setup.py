from data.queries import sql_queries

from database.sql import db

async def setup_tables():
    for query in sql_queries:
        await db.execute(query, execute=True)
