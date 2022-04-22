from aiogram import Bot, Dispatcher, types
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_start(message: types.Message):
    await message.answer("Hello Grindel!")


@dp.message_handler()
async def sender(message: types.Message):
    await message.answer(message.text)
