from bot.bot import dp
from aiogram.types import Message
from keyboards.user.reply_buttons.start_buttons import start_commands_buttons


@dp.message_handler(commands=["start", "старт"])
async def command_start(msg: Message):
    await msg.answer(
        text=f"✨ <b>Добро пожаловать в « Числа Судьбы »</b>, @{msg.from_user.username}! 👋🤖\n"
             f"\nС моей помощью вы сможете раскрыть тайны вашей жизни:\n"
             f"    🛤️ <b>Число жизненного пути</b> — узнайте своё предназначение!\n"
             f"    🔮 <b>Число Судьбы</b> — расшифруйте скрытые возможности!\n"
             f"    💞 <b>Совместимость с партнёром</b> — проверьте гармонию ваших отношений!\n"
             f"    💪 <b>Совместимость с другом</b> — откройте секреты гармонии и силы ваших дружеских отношений!\n"
             f"    💖 <b>Число Души. Внутренние желания</b> — рассчитайте своё число души и узнайте о глубинных желаниях и мотивах, которые движут вами!\n"
             f"\n📘 Нужна помощь?\nНапишите <b>/help</b> или выберите команду в меню 📋✨\n"
             f"<i>Пусть магия чисел ведёт вас к успеху!</i> 🔢",
        parse_mode="HTML",
        reply_markup=start_commands_buttons
    )