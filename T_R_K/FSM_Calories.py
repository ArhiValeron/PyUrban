from aiogram import F, Router
from aiogram.filters import StateFilter
from aiogram.types import (Message, CallbackQuery)
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from Keyboards import make_row_keyboard


router = Router(name=__name__)

genders = ["Мужской", "Женский"]
class UserState(StatesGroup):
    gender = State()
    age = State()
    weight = State()
    growth = State()

async def callories(weidht, growth, age, gender):
    if gender == "Мужской":
        ret = (10 * weidht) + (6.25 * growth) - (5 * age) + 5
    if gender == "Женский":
        ret = (10 * weidht) + (6.25 * growth) - (5 * age) - 161
    return ret

@router.message(F.text == "стоп")
async def stop_calories(message: Message, state: FSMContext):
    await message.answer("Опрос прерван, для возврата в меню "
                         "воспользуйтесь командой /start")
    await state.clear()

@router.callback_query(StateFilter(None), F.data == "calories_math")
async def cmd_callories(callback: CallbackQuery, state: FSMContext):
    # Устанавливаем пользователю состояние "выбирает пол"
    await state.set_state(UserState.gender)
    await callback.answer("Пройдите небольшой опрос для уточнения данных,"
                          " что бы выйти из опроса в любой момент напишите "
                          "'стоп'.", show_alert=True)
    await callback.message.answer(
        text="Подскажите, какого вы пола:",
        reply_markup=make_row_keyboard(genders, )
    )


@router.message(UserState.gender)
async def callories_gender(message: Message, state: FSMContext):
    if message.text == "Женский" or message.text == "Мужской":
        await state.update_data(gender=message.text)
        await message.answer("Сколько Вам полных лет?")
        await state.set_state(UserState.age)

    else:
        await message.answer("Используйте кнопки для определения пола \n"
                             "Male - Мужской. \n"
                             "Female - Женский", reply_markup=make_row_keyboard(genders))


@router.message(UserState.age)
async def callories_age(message: Message, state: FSMContext):
    try:
        age = int(message.text)
        if 5 < age < 120:
            await message.answer("Сколько вы весите в кг? Введите целое число")
            await state.update_data(age=age)
            await state.set_state(UserState.weight)
        else:
            await message.answer("Возраст должен быть в диапазоне от 5 до 120 лет.")
    except ValueError:
        await message.answer("Пожалуйста, введите целое число.")


@router.message(UserState.weight)
async def callories_weight(message: Message, state: FSMContext):
    try:
        weight = int(message.text)
        if weight > 0:
            await state.update_data(weight=weight)
            await message.answer("Введите свой рост в см: ")
            await state.set_state(UserState.growth)
        else:
            await message.answer("Вес должен быть целым положительным числом.")
    except ValueError:
        await message.answer("Пожалуйста, введите целое число для веса.")

@router.message(UserState.growth)
async def callories_growth(message: Message, state: FSMContext):
    try:
        growth = int(message.text)
        if growth > 0:
            await state.update_data(growth=growth)
            data = await state.get_data()
            await message.answer(f"Полученные данные: {data}")
            result = await callories(data['weight'], data['growth'], data['age'], data['gender'])
            await message.answer(f"Ваша рекомендуемая норма калорий: {result}")
            await state.clear() # Очищаем состояние после завершения
        else:
            await message.answer("Рост должен быть положительным числом.")
    except ValueError:
        await message.answer("Пожалуйста, введите целое число для роста.")
    except KeyError as e:
        await message.answer(f"Ошибка: Недостаточно данных. {e}")
        await state.clear()  # Очищаем состояние для выхода из последовательности

