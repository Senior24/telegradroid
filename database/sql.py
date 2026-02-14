import json

from .postgresql import PostgreSQL

class Database(PostgreSQL):
    async def add_user(self, user_id, first_name, last_name, username, lang):
        sql = "INSERT INTO bot.users (user_id, first_name, last_name, username, lang) VALUES($1, $2, $3, $4, $5)"
        return await self.execute(sql, user_id, first_name, last_name, username, lang, execute=True)

    async def update_user(self, user_id, first_name, last_name, username, last_seen):
        sql = "UPDATE bot.users SET first_name = $1, last_name = $2, username = $3, last_seen = $4 WHERE user_id = $5"
        return await self.execute(sql, first_name, last_name, username, last_seen, user_id, execute=True)

    async def check_user(self, user_id):
        sql = "SELECT * FROM bot.users WHERE user_id = $1"
        return bool(await self.execute(sql, user_id, fetch=True))

    async def lang(self, user_id):
        sql = "SELECT lang FROM bot.users WHERE user_id = $1"
        return await self.execute(sql, user_id, fetch_val=True)

    async def apps(self, user_id):
        sql = "SELECT apps FROM bot.users WHERE user_id = $1"
        result = await self.execute(sql, user_id, fetch_val=True)
        return json.loads(result)

    async def add_app(self, user_id, app, thread_id):
        sql = f"UPDATE bot.users SET apps = coalesce(apps, '{{}}'::jsonb) || jsonb_build_object('{app}', {thread_id}) WHERE user_id = $1"
        await self.execute(sql, user_id, execute=True)

    async def remove_app(self, user_id, *apps):
        sql = "UPDATE bot.users SET apps = apps - $1 WHERE user_id = $2"
        await self.execute(sql, str(apps), user_id, execute=True)

    async def app_thread_id(self, user_id, app):
        sql = "SELECT data->>'$2' FROM bot.users WHERE user_id = $1"
        return await self.execute(sql, user_id, app, fetch_val=True)

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetch_row=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM Users"
        return await self.execute(sql, fetch_val=True)

    async def update_user_username(self, username, telegram_id):
        sql = "UPDATE Users SET username=$1 WHERE telegram_id=$2"
        return await self.execute(sql, username, telegram_id, execute=True)

    async def delete_users(self):
        await self.execute("DELETE FROM Users WHERE TRUE", execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE Users", execute=True)


db = Database()
