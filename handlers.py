import os
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions
from my_token import TOKEN
import defs
from aiogram.dispatcher.filters.state import State, StatesGroup

API_TOKEN = TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



class Host(StatesGroup):
    host = State()


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    msg = text(bold('Я могу ответить на следующие команды:'),
               '/connection', '/del', sep='\n')
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)

@dp.message_handler(commands=['connection'])
async def get_hostport(message: types.Message):
    await message.answer('Введите хост и порт (напр. 93.159.102.225:5432)')
    await Host.host.set()

@dp.message_handler(commands=['del'])
async def get_hostport(message: types.Message):
    await message.answer(Host.host)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)