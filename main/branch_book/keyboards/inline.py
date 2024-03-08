from aiogram.utils.keyboard import InlineKeyboardBuilder


def choice_restaurant():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="lafa", callback_data="choose_lafa")
    keyboard_builder.button(text="kaif", callback_data="choose_kaif")

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()