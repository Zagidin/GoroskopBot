"""
    Число жизненного пути
"""

from bot.bot import dp
from aiogram.types import Message


@dp.message_handler(text="🛤️ Число жизненного пути")
async def life_path_number(msg: Message):
    pass