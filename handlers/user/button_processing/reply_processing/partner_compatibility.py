"""
    Совместимость с партнёром
"""

from bot.bot import dp
from aiogram.types import Message


@dp.message_handler(text="💞 Совместимость с партнёром")
async def partner_compatibility(msg: Message):
    pass