#используется aiogram 3х
import asyncio
import logging

from aiogram import Bot, Dispatcher, F, html, Router
from aiogram.filters import CommandStart, Command, CommandObject, StateFilter
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
    weidht = State()
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
    await message.answer(f"Привет! {html.bold(html.quote(message.from_user.full_name))}! \n"
                         f"Я бот помогающий твоему здоровью. \n"
                         f"Твой ID:{message.from_user.id} \n"
                         f"Что бы узнать рекомендуемую норму калорий используй команду /callories \n"
                         f"Что бы получить помощь используй команду /help \n"
                         , parse_mode="HTML")


@dp.message(Command('help'))
async def get_help(message: Message):
    await message.answer("К сожалению, Вас уже не спасти.")


@dp.message(Command("hello"))
async def cmd_hello(message: Message):
    await message.answer(
        f"Hello, {html.bold(html.quote(message.from_user.full_name))}",
        parse_mode="HTML"
    )


@dp.message(F.text == "Я буду жить?")
async def get_life(message: Message):
    await message.answer("Конечно, будете!")


@router.message(StateFilter(None), Command("callories"))
async def cmd_callories(message: Message, state: FSMContext):
    await message.answer(
        text="Подскажите, какого вы пола:",
        reply_markup=make_row_keyboard(genders)
    )
    # Устанавливаем пользователю состояние "выбирает название"
    await state.set_state(UserState.gender)


#Необработанные
"""@dp.message(F.text != "")
async def get_life(message: Message):
    await message.answer("Введите команду /start, чтобы начать общение.")"""


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
