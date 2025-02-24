"""
    Дальше
"""

from bot.bot import dp
from aiogram.types import Message


@dp.message_handler(text="🚀 Дальше ➡️")
async def next_button(msg: Message):
    await msg.answer(
        text="Пока в Разработке!"
    )