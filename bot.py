import logging
import asyncio
import os

from aiogram.fsm.storage.memory import MemoryStorage

from utils.create_pool_db import create_pool

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from middlewares.dbmiddleware import DbSession
from utils.commands import set_commands

from main.handlers import start_choice_branch
from main.branch_book.handlers import choice_rest
from main.branch_book.branch_lafa.handlers import choice_table_lafa

from main.branch_admin.handlers import choice_res_adm
from main.branch_admin.branch_amd_lafa.handlers import adm_lafa

from main.gpt_chat import start_gpt


load_dotenv()

TG_API_TOKEN = os.getenv('TG_API_TOKEN')


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(492500841, text="Бот запущен")


async def stop_bot(bot: Bot):
    await bot.send_message(492500841, text="Бот остановлен")


async def main():
    # Пишет инфо логи в консоль
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s -"
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")

    # Импортирует токен из файла .env
    bot = Bot(token=TG_API_TOKEN)

    # Конект к БД
    pool_connect = await create_pool()

    # Диспетчер
    dp = Dispatcher(storage=MemoryStorage())

    # Создает подключение к БД
    dp.update.middleware.register(DbSession(pool_connect))

    # Срабатывают при запуске и остановке бота
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    # Выбор ветки
    dp.include_routers(start_choice_branch.router)

    # Выбор ресторана
    dp.include_routers(choice_rest.router)

    # Выбор стола в лафе
    dp.include_routers(choice_table_lafa.router)

    # Ветка для владельцев ресторанов
    dp.include_routers(choice_res_adm.router)

    # Админ панель для lafa
    dp.include_routers(adm_lafa.router)

    # GPT бот
    dp.include_routers(start_gpt.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())