from aiogram import Router, F
from aiogram.types import CallbackQuery

from asyncpg.exceptions import UniqueViolationError


from main.branch_book.branch_lafa.keyboards.inline import choice_table_bt
from utils.dbconnect import Request

router = Router()  # [1]


@router.callback_query(F.data == "choose_lafa")  # [2]
async def choice_table(callback: CallbackQuery):
    await callback.message.answer(
        "Выберите столик, имя указывать не нужно оно автоматически запишется с вашего тг:",
        reply_markup=choice_table_bt())


@router.callback_query(lambda c: c.data.startswith('table№_'))  # [2]
async def choice_table(callback: CallbackQuery, request: Request):
    try:
        await request.book_table_lafa(callback.from_user.id, callback.from_user.first_name, callback.data[7])
        await callback.message.answer(f"Стол № {callback.data[7]} успешно забронирован")
    except UniqueViolationError:
        await callback.message.answer(f"Вы не можете забронировать больше одного стола!")
