from aiogram import Router, F
from aiogram.types import Message


from main.branch_book.keyboards.inline import choice_restaurant

router = Router()  # [1]


@router.message(F.text == "Хочу забронировать столик")  # [2]
async def start_choice_restaurant(message: Message):
    await message.answer(
        "Выберите ресторан:",
        reply_markup=choice_restaurant()
    )