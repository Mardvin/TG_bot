# import os
#
# from dotenv import load_dotenv
# from aiogram import Router, F
# from aiogram.types import Message
#
# from openai import OpenAI
# from main.branch_book.keyboards.inline import choice_restaurant
#
# load_dotenv()
#
# GPT_API_TOKEN = os.getenv('GPT_API_TOKEN')
#
#
# def get_gpt_client():
#     client = OpenAI(
#         api_key=GPT_API_TOKEN,
#         base_url="https://api.proxyapi.ru/openai/v1",
#     )
#
#     return client
#
#
# router = Router()  # [1]
#
#
# @router.message(F.text == "Посоветуй мне рестораны")  # [2]
# async def start_choice_restaurant(message: Message):
#     await message.answer(
#         "Привет, я Ваш помощник с выбором ресторана",
#     )
#
#
# chat = get_gpt_client().chat.completions.create(
#     model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Порекомендуй мне рестораны"}]
# )
#
# print(chat.choices[0].message.content)

import os

from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, Router, F


from openai import OpenAI

load_dotenv()

GPT_API_TOKEN = os.getenv('GPT_API_TOKEN')


class RestaurantDialog(StatesGroup):
    waiting_for_restaurant_recommendation = State()


def get_gpt_client():
    client = OpenAI(
        api_key=GPT_API_TOKEN,
        base_url="https://api.proxyapi.ru/openai/v1",
    )
    return client


router = Router()


@router.message(F.text == "Посоветуй мне рестораны")
async def start_choice_restaurant(message: Message, state: FSMContext):
    await state.set_state(RestaurantDialog.waiting_for_restaurant_recommendation)
    await message.answer("Пожалуйста, укажите свои предпочтения или локацию для ресторана.")


@router.message(RestaurantDialog.waiting_for_restaurant_recommendation)
async def get_restaurant(message: Message, state: FSMContext):
    client = get_gpt_client()
    chat = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message.text}]
    )
    response_text = chat.choices[0].message.content
    print(response_text)
    await message.answer(response_text)
    await state.clear()  # Завершаем сессию после ответа

