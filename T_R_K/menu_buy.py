from aiogram import F, Router

from aiogram.types import (CallbackQuery)

router = Router(name=__name__)
@router.callback_query(F.data == "product_buying")
async def get_life(message: CallbackQuery):
    await message.message.answer("Покупка совершена!")
    await message.answer("")
