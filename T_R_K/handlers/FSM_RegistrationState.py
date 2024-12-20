from aiogram import F, Router
from aiogram.filters import StateFilter
from aiogram.types import (Message, CallbackQuery)
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from T_R_K.Fill_db import db_user_is_included, db_add_user, db_commit


router = Router(name=__name__)


class UserAdd(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()


@router.callback_query(StateFilter(None), F.data == "add_user")
async def new_user(callback: CallbackQuery, state: FSMContext):
    await state.set_state(UserAdd.username)
    await callback.answer("Пройдите небольшой опрос для уточнения данных,"
                          " что бы выйти из опроса в любой момент напишите "
                          "'стоп'.", show_alert=True)
    await callback.message.answer(text="Подскажите, как Вас зовут:")

@router.message(UserAdd.username)
async def add_username(message: Message, state: FSMContext):
    if db_user_is_included(message.text):
        await message.answer(f"Имя пользователя существует, \n"
                             f"пожалуйста выберите другое.")
    else:
        await state.update_data(username=message.text)
        await message.answer("Напишите Вашь email")
        await state.set_state(UserAdd.email)

@router.message(UserAdd.email)
async def add_user_mail(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer("Сколько Вам полных лет?")
    await state.set_state(UserAdd.age)

@router.message(UserAdd.age)
async def add_user_age(message: Message, state: FSMContext):
    try:
        age = int(message.text)
        if 5 < age < 120:
            await state.update_data(age=age)
            await state.update_data(balance=1000)
            await state.update_data(tgid=message.from_user.id)

            data = await state.get_data()
            await message.answer(f"Полученные данные: {data}")
            db_add_user(data["username"],data["email"],data["age"],data["balance"],data["tgid"])
            db_commit()
            await state.clear()
        else:
            await message.answer("Возраст должен быть в диапазоне от 5 до 120 лет.")
    except ValueError:
        await message.answer("Пожалуйста, введите целое число.")
    except KeyError as e:
        await message.answer(f"Ошибка: Недостаточно данных. {e}")
        await state.clear()





