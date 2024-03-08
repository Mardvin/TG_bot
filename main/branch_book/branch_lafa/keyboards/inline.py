from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def choice_table_bt() -> InlineKeyboardMarkup:
    """
    Старт тг бота, определяет к какой категории относишься
    :return:
    """
    kb = InlineKeyboardBuilder()
    kb.button(text="стол №1", callback_data="table№_1")
    kb.button(text="стол №2", callback_data="table№_2")
    kb.button(text="стол №3", callback_data="table№_3")
    kb.button(text="стол №4", callback_data="table№_4")
    kb.button(text="стол №5", callback_data="table№_5")
    kb.button(text="стол №6", callback_data="table№_6")
    kb.button(text="стол №7", callback_data="table№_7")
    kb.button(text="стол №8", callback_data="table№_8")
    kb.button(text="стол №9", callback_data="table№_9")
    kb.adjust(3, 3, 3)
    return kb.as_markup()
