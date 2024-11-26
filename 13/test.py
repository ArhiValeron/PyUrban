import os
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import logging
from app.handlers import router
load_dotenv()
async def main():
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
try:
    asyncio.run(main())
except:
    print('Exit')