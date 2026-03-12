from database.sql import Database as DB

class Database(DB):
   async def get_data(self, column: str, arg: str, check_by: str):
      sql = f"SELECT {column} FROM file_link.storage WHERE {check_by} = $1"
      return await self.execute(sql, arg, fetch_val=True)

   async def add_record(self, file_id: str, content_type: str, code: str):
      sql = "INSERT INTO file_link.storage (file_id, content_type, code) VALUES ($1, $2, $3)"
      await self.execute(sql, file_id, content_type, code, execute=True)

