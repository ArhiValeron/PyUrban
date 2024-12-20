#используется aiogram 3х

from aiogram import F, Router
from aiogram.types import (Message)

router = Router(name=__name__)


@router.message()
async def get_life(message: Message):
    await message.answer("Введите команду /start, чтобы начать общение.")

@router.message(F.text == "Я буду жить?")
async def get_life(message: Message):
    await message.answer("Конечно, будете!")