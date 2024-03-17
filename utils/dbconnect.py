import asyncpg


class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def book_table_lafa(self, id_user, name, number_tb):
        query = f"INSERT INTO data_table_lafa (id_user, name, num_table)" \
                f"VALUES ('{id_user}', '{name}', '{number_tb}');"
        await self.connector.execute(query)

    async def get_data_lafa(self):
        query = f"SELECT * FROM data_table_lafa"
        data = await self.connector.fetch(query)
        return data

    async def delete_data_by_id(self, id):
        query = f"DELETE FROM data_table_lafa WHERE id_user = $1"
        await self.connector.execute(query, id)


