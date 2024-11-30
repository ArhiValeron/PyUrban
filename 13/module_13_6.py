#используется aiogram 3х
import asyncio
import logging

from aiogram import Bot, Dispatcher, F, html, Router
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.chat_action import ChatActionSender

from config import bot_token as TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())
router = Router(name=__name__)
dp.include_router(router)
#Константы
genders = ["Male", "Female"]


#Классы
class UserState(StatesGroup):
    gender = State()
    age = State()
    weight = State()
    growth = State()


#Вспомогательные функции
async def callories(weidht, growth, age, gender):
    if gender == "Male":
        ret = (10 * weidht) + (6.25 * growth) - (5 * age) + 5
    if gender == "Female":
        ret = (10 * weidht) + (6.25 * growth) - (5 * age) - 161
    return ret


def make_row_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
    """
    Создаёт реплай-клавиатуру с кнопками в один ряд
    :param items: список текстов для кнопок
    :return: объект реплай-клавиатуры
    """
    row = [KeyboardButton(text=item) for item in items]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)


#Обработчики сообщений
my_router = Router(name=__name__)


@dp.message(CommandStart())  #Кнопка /Start
async def cmd_start(message: Message):
    await message.answer(text=f"Привет! {html.bold(html.quote(message.from_user.full_name))}! \n"
                         f"Я бот помогающий твоему здоровью. \n"
                         f"Твой ID:{message.from_user.id} \n"
                         f"Что бы узнать рекомендуемую норму калорий кнопку Рассчитать \n"
                         f"Что бы получить помощь используй команду /help \n"
                         , parse_mode="HTML", reply_markup=make_row_keyboard(["Рассчитать", "Информация"]))


@dp.message(Command('help'))
async def get_help(message: Message):
    await message.answer("К сожалению, Вас уже не спасти.")


@dp.message(Command("hello"))
async def cmd_hello(message: Message):
    await message.answer(
        f"Hello, {html.bold(html.quote(message.from_user.full_name))}",
        parse_mode="HTML"
    )


@dp.message(F.text == "Информация")
async def get_life(message: Message):
    await message.answer("Тут могла бы быть Ваша реклама!")


@dp.message(F.text == "Я буду жить?")
async def get_life(message: Message):
    await message.answer("Конечно, будете!")


#FSM command callories
@dp.message(StateFilter(None), F.text == "Рассчитать")
async def cmd_callories(message: Message, state: FSMContext):
    await message.answer(
        text="Подскажите, какого вы пола:",
        reply_markup=make_row_keyboard(genders)
    )
    # Устанавливаем пользователю состояние "выбирает пол"
    await state.set_state(UserState.gender)


@dp.message(UserState.gender)
async def callories_gender(message: Message, state: FSMContext):
    if message.text == "Female" or message.text == "Male":
        await state.update_data(gender=message.text)
        await message.answer("Сколько Вам полных лет?")
        await state.set_state(UserState.age)
    else:
        await message.answer("Используйте кнопки для определения пола \n"
                             "Male - Мужской. \n"
                             "Female - Женский")


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
