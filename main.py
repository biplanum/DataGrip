import os
import logging
from aiogram import Bot, Dispatcher, executor, types
from my_token import TOKEN

API_TOKEN = TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)