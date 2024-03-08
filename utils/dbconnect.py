import asyncpg


class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def book_table_lafa(self, id_user, name, number_tb):
        query = f"INSERT INTO data_table_lafa (id_user, name, num_table)" \
                f"VALUES ('{id_user}', '{name}', '{number_tb}');"
        await self.connector.execute(query)

    async def add_form_hotel(self, user_id, name_hotel, address_hotel, phone, photo):
        query = f"INSERT INTO data_hotel (user_id, name_hotel, address, phone, photo)" \
                f"VALUES ('{user_id}', '{name_hotel}', '{address_hotel}', '{phone}', '{photo}');"
        await self.connector.execute(query)

    # async def update_form_hotel(self, user_id, name_hotel, address_hotel, phone, photo):
    #     query = f"INSERT INTO data_hotel (user_id, name_hotel, address, phone, photo)" \
    #             f"VALUES ('{user_id}', '{name_hotel}', '{address_hotel}', '{phone}', '{photo}');"
    #     await self.connector.execute(query)

    async def get_form_worker(self):
        query = f"SELECT * FROM data_worker_search"
        data = await self.connector.fetch(query)
        return data

    async def create_vacancy_horika(self, user_id, city, user_name, position, employment, experience, wages):
        query = f"INSERT INTO vacancy_horika (user_id, city, user_name, position, employment, experience, wages)" \
                f"VALUES ('{user_id}', '{city}', '{user_name}', '{position}', '{employment}', '{experience}', '{wages}');"
        await self.connector.execute(query)

    async def get_vacancy_horika(self, city):
        query = f"SELECT * FROM vacancy_horika WHERE city = '{city}';"
        data = await self.connector.fetch(query)
        return data



