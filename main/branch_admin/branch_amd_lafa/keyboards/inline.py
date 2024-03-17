from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def adm_lafa_bt() -> InlineKeyboardMarkup:
    """
    Старт тг бота, определяет к какой категории относишься
    :return:
    """
    kb = InlineKeyboardBuilder()
    kb.button(text="Показать бронь", callback_data="show_table_lafa")
    kb.button(text="Удалить бронь", callback_data="delete_book")
    kb.adjust(1)
    return kb.as_markup()