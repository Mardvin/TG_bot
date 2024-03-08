import logging
import asyncio

from utils.create_pool_db import create_pool

from aiogram import Bot, Dispatcher
from config_reader import config

from middlewares.dbmiddleware import DbSession
from utils.commands import set_commands

from main.handlers import start_choice_branch
from main.branch_book.handlers import choice_rest
from main.branch_book.branch_lafa.handlers import choice_table_lafa


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
    bot = Bot(token=config.bot_token.get_secret_value())

    # Конект к БД
    pool_connect = await create_pool()

    # Диспетчер
    dp = Dispatcher()

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

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())