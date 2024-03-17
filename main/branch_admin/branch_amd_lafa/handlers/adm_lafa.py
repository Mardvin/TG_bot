from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from main.branch_admin.branch_amd_lafa.keyboards.inline import adm_lafa_bt

from main.branch_admin.branch_amd_lafa.filters.statesform import StepsForm

from utils.dbconnect import Request

router = Router()  # [1]


@router.callback_query(F.data == "choose_lafa_adm")  # [1]
async def choice_res(callback: CallbackQuery):
        await callback.message.answer(f"Ведите пароль для входа в адин панель: ")


@router.message(F.text == "lafa")  # [2]
async def enter(message: Message):
    await message.answer(
        "Административная панель lafa",
        reply_markup=adm_lafa_bt()
    )


def get_str(data: list) -> str:
    string = ""
    for info in data:
        string += f"№ стола: {info[2]}, имя: {info[1]}, id: {info[0]}\n"
    return string


@router.callback_query(F.data == "show_table_lafa")
async def show_table_lafa(callback: CallbackQuery, request: Request):
    data_info_table = await request.get_data_lafa()
    info = get_str(data_info_table)
    await callback.message.answer(f"{info}")


@router.callback_query(F.data == "delete_book")
async def delete_book(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(f"Ведите id брони")
    await state.set_state(StepsForm.GET_ID)


@router.message(StepsForm.GET_ID)
async def get_id(message: Message, state: FSMContext, request: Request):
    await request.delete_data_by_id(int(message.text))
    await message.answer("Бронь успешно удалена")
    await state.clear()

