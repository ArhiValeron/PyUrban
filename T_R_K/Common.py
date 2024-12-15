#используется aiogram 3х
import asyncio
import logging

from aiogram import Bot, Dispatcher, F, html, Router
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import (Message, ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery)
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage

from Keyboards import make_row_keyboard


router = Router(name=__name__)


@router.message()
async def get_life(message: Message):
    await message.answer("Введите команду /start, чтобы начать общение.")

@router.message(F.text == "Я буду жить?")
async def get_life(message: Message):
    await message.answer("Конечно, будете!")