from bot.bot import dp
from aiogram.types import Message
from keyboards.user.reply_buttons.start_buttons import start_commands_buttons


@dp.message_handler(commands=["help", "помощь"])
async def command_start(msg: Message):
    await msg.answer(
        text="Пока чисто, Команды внизу 👇",
        reply_markup=start_commands_buttons
    )