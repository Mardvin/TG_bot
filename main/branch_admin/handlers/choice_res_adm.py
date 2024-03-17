from aiogram import Router, F
from aiogram.types import Message


from main.branch_admin.keyboards.inline import choice_restaurant_adm

router = Router()  # [1]


@router.message(F.text == "Владею рестораном")  # [2]
async def start_choice_restaurant(message: Message):
    await message.answer(
        "Вкладка для администрации ресторанов.\nВыберите свой ресторан:",
        reply_markup=choice_restaurant_adm()
    )