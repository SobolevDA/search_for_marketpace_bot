from aiogram import executor
from app.bot import dp
import logging

logging.basicConfig(level=logging.DEBUG, filename="app.log", filemode="w", format='%(name)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
