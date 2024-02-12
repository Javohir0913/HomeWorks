import asyncio
import sys
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher
from config import TOKEN
import logging
from handlers.msg_handlers import msg_router
from handlers.cmd_handlers import cmd_router

async def main():
    dp = Dispatcher()
    dp.include_routers(cmd_router, msg_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
try:
    asyncio.run(main())

except KeyboardInterrupt:
    print("bot to'xtatildi")