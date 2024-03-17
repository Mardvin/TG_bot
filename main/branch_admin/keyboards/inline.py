from aiogram.utils.keyboard import InlineKeyboardBuilder


def choice_restaurant_adm():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="lafa", callback_data="choose_lafa_adm")
    keyboard_builder.button(text="kaif", callback_data="choose_kaif_adm")

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()