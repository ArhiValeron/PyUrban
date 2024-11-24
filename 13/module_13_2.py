#используется aiogram 3х
import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from bot_inf import bot_token as TOKEN

bot = Bot(token = TOKEN)
dp = Dispatcher()

#Обработчики сообщений
@dp.message(CommandStart()) #Кнопка /Start
async def cmd_start(message: Message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

@dp.message(Command('help'))
async def get_help(message: Message):
    await message.answer("К сожалению, Вас уже не спасти.")

@dp.message(F.text == "Я буду жить?")
async def get_life(message: Message):
    await message.answer("Конечно будете!")

#Необработанные
@dp.message(F.text != "")
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