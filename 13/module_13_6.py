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

from config import bot_token as TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())
#Инлайн клавиатуры

kb_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Рассчет калорий", callback_data="calories_math")],
    [InlineKeyboardButton(text="Помощь", callback_data="help")],
    [InlineKeyboardButton(text="Приветствие", callback_data="hello")],
    [InlineKeyboardButton(text="Иформация", callback_data="info")]
])



#Константы
genders = ["Мужской", "Женский"]


#Классы
class UserState(StatesGroup):
    gender = State()
    age = State()
    weight = State()
    growth = State()

#Флаги



#Функции
async def callories(weidht, growth, age, gender):
    if gender == "Мужской":
        ret = (10 * weidht) + (6.25 * growth) - (5 * age) + 5
    if gender == "Женский":
        ret = (10 * weidht) + (6.25 * growth) - (5 * age) - 161
    return ret


def make_row_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
    """
    Создаёт реплай-клавиатуру с кнопками в один ряд
    :param items: список текстов для кнопок
    :return: объект реплай-клавиатуры
    """
    row = [KeyboardButton(text=item) for item in items]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True,
                               one_time_keyboard=True,
                               input_field_placeholder="Воспользуйтесь кнопками ниже." )



#Обработчики сообщений ------------------------------------------------------------
my_router = Router(name=__name__)


@dp.message(CommandStart())  #Кнопка /Start
async def cmd_start(message: Message):
    await message.answer(text=f"Привет! {html.bold(html.quote(message.from_user.full_name))}! \n"
                         f"Я бот помогающий твоему здоровью. \n"
                         f"Твой ID:{message.from_user.id} \n"
                         , parse_mode="HTML", reply_markup=kb_main)


@dp.callback_query(F.data == 'help')
async def get_help(callback: CallbackQuery):
    await callback.answer("Помощь уже близко! Держитесь!")


@dp.callback_query(F.data == "hello")
async def cmd_hello(callback: CallbackQuery):
    await callback.message.answer(
        f"Привет, {html.bold(html.quote(callback.from_user.full_name))}",
        parse_mode="HTML"
    )
    await callback.answer("")


@dp.callback_query(F.data == "info")
async def get_life(message: CallbackQuery):
    await message.answer(f"Кривобот написан, студентом университета Urban \n"
                         f" Бурдиным Валерием Валерьевичем\n"
                         f"Возможно все права защищены, но это не точно.\n"
                         f"@TechnoBUG", show_alert=True)


@dp.message(F.text == "Я буду жить?")
async def get_life(message: Message):
    await message.answer("Конечно, будете!")


#FSM command calories ========================================================
@dp.message(F.text == "стоп")
async def stop_calories(message: Message, state: FSMContext):
    await message.answer("Опрос прерван, для возврата в меню воспользуйтесь командой /start")
    await state.clear()

@dp.callback_query(StateFilter(None), F.data == "calories_math")
async def cmd_callories(callback: CallbackQuery, state: FSMContext):
    # Устанавливаем пользователю состояние "выбирает пол"
    await state.set_state(UserState.gender)
    await callback.answer("Пройдите небольшой опрос для уточнения данных,"
                          " что бы выйти из опроса в любой момент напишите 'стоп'.", show_alert=True)
    await callback.message.answer(
        text="Подскажите, какого вы пола:",
        reply_markup=make_row_keyboard(genders, )
    )


@dp.message(UserState.gender)
async def callories_gender(message: Message, state: FSMContext):
    if message.text == "Женский" or message.text == "Мужской":
        await state.update_data(gender=message.text)
        await message.answer("Сколько Вам полных лет?")
        await state.set_state(UserState.age)

    else:
        await message.answer("Используйте кнопки для определения пола \n"
                             "Male - Мужской. \n"
                             "Female - Женский", reply_markup = make_row_keyboard(genders))


@dp.message(UserState.age)
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


@dp.message(UserState.weight)
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

@dp.message(UserState.growth)
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



#Необработанные
@dp.message()
async def get_life(message: Message):
    await message.answer("Введите команду /start, чтобы начать общение.")


#Кривой стартер для бота
async def main():
    await dp.start_polling(bot)


#########################################################################################
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)  #отключить после отладки
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit by KeyboardInterrupt")
