
from aiogram import F, html, Router
from aiogram.filters import CommandStart
from aiogram.types import (Message, CallbackQuery)

from T_R_K.KeyBoards.keyboards import kb_main
from T_R_K.keybordbuilder import kb_catalog


router = Router(name=__name__)


@router.message(CommandStart())  #Кнопка /Start
async def cmd_start(message: Message):
    await message.answer(text=f"Привет! {html.bold(html.quote(message.from_user.full_name))}! \n"
                         f"Я бот помогающий твоему здоровью. \n"
                         f"Твой ID:{message.from_user.id} \n"
                         , parse_mode="HTML")
    await message.answer(text="Главное меню:",
                         reply_markup=kb_main)


@router.callback_query(F.data == 'help')
async def get_help(callback: CallbackQuery):
    await callback.answer("Помощь уже близко! Держитесь!")


@router.callback_query(F.data == "hello")
async def cmd_hello(callback: CallbackQuery):
    await callback.message.answer(
        f"Привет, {html.bold(html.quote(callback.from_user.full_name))}",
        parse_mode="HTML"
    )
    await callback.answer("")


@router.callback_query(F.data == "info")
async def get_life(message: CallbackQuery):
    await message.answer(f"Кривобот создан студентом университета Urban, \n"
                         f" Бурдиным Валерием Валерьевичем\n"
                         f"Все права защищены, но это не точно.\n"
                         f"Arhivaleron@yandex.ru", show_alert=True)

@router.callback_query(F.data == "buy_menu")
async def get_life(message: CallbackQuery):
    await message.message.edit_text("Каталог:", reply_markup=kb_catalog)
    await message.answer("Вы перешли в каталог")
