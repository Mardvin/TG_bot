from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def start_button() -> ReplyKeyboardMarkup:
    """
    Старт тг бота, определяет к какой категории относишься
    :return:
    """
    kb = ReplyKeyboardBuilder()
    kb.button(text="Посоветуй мне рестораны")
    kb.button(text="Хочу забронировать столик")
    kb.button(text="Владею рестораном")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)