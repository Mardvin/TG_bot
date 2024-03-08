from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from utils.dbconnect import Request

from main.keyboards.start_choice import start_button

router = Router()  # [1]


@router.message(Command("start"))  # [2]
async def cmd_start(message: Message, request: Request):
    await message.answer(
        "Вас приветствует телеграм бот N пожалуйста выберите категорию к который вы относитесь",
        reply_markup=start_button()
    )
