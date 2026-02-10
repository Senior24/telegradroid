from .postgresql import PostgreSQL

class Database(PostgreSQL):
    async def add_user(self, user_id, first_name, last_name, username):
        sql = "INSERT INTO bot.users (user_id, first_name, last_name, username) VALUES($1, $2, $3, $4)"
        return await self.execute(sql, user_id, first_name, last_name, username, execute=True)

    async def update_user(self, user_id, first_name, last_name, username):
        sql = "UPDATE bot.users SET first_name=$1, last_name=$2, username=$3 WHERE user_id=$4"
        return await self.execute(sql, first_name, last_name, username, user_id, execute=True)

    async def check_user(self, user_id):
        sql = "SELECT * FROM bot.users WHERE user_id = $1"
        return bool(await self.execute(sql, user_id, fetch=True))

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
