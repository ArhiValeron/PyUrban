#используется aiogram 3х
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from routers import main_router

from key import bot_token as TOKEN

from Fill_db import db_close

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())
dp.include_router(main_router)


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
    finally:
        db_close()

