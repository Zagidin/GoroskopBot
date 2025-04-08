"""
    Число Судьбы
"""

import asyncio
import random

from bot.bot import dp
from aiogram.types import (
    Message,
    ReplyKeyboardRemove
)
from aiogram.dispatcher import FSMContext
from ai.request_to_ai import request_to_ai
from status_machine.date_of_birth import DateOfBirth
from keyboards.user.reply_buttons.start_buttons import start_commands_buttons


@dp.message_handler(text="🔮 Число Судьбы")
async def destiny_number(msg: Message):
    await msg.answer(
        text="✨ <b>Давайте раскроем тайны вашего Числа Судьбы</b> 🔮🌟\n"
             "\n📅 Введите дату рождения в формате по примеру ниже:\n"
             "    <i>\nНапример</i>:\n"
             "        <b>17.08.2007</b>\n"
             "\n<i>Пусть звёзды подскажут вашу уникальную дорогу!</i> 💫",
        parse_mode="HTML",
        reply_markup=ReplyKeyboardRemove()
    )

    await DateOfBirth.user_date_of_birth.set()

@dp.message_handler(state=DateOfBirth.user_date_of_birth)
async def user_date_of_birth_text(msg: Message, state: FSMContext):

    """
        💡 variable num_fate: Число судьбы пользователя по дате рождения
    """

    global num_fate

    async with state.proxy() as data:
        data["user_date_of_birth"] = msg.text

    if data["user_date_of_birth"]:
        if "." in data["user_date_of_birth"][:3] and "." in data["user_date_of_birth"][-5:]:
            if data["user_date_of_birth"].replace(".", "").isdigit():

                async with state.proxy() as data:
                    data["num_fate"] = sum([int(num) for num in data["user_date_of_birth"].replace(".", "")])

                await state.finish()

                num_fate = sum([int(num) for num in str(data["num_fate"])])

                if num_fate > 9:
                    num_fate = sum([int(num) for num in str(num_fate)])
        else:
            await msg.answer(
                text=f"Что-то пошло не так, некорректно набрана дата рождения, возможно вы не прописали разделительный знак \".\" ! "
                     f"Введите дату рождения по примеру {random.choice(['🤔', '😔'])}"
            )

    request = f"""
        Сгенерируй нумерологический отчёт на русском языке по числу {num_fate}
    
        Структура Вывода сделай такую:
        🔢 Число Судьбы: число
         
        🧠 Влияние на личность: 1-2 предложения о характере
         
        🌟 Предназначение: Главная жизненная миссия 
        
        💡 Совет: Практическая рекомендация
    
        P.S можешь ещё от себя накидать информации интересной 😎
        Заранее спасибо! и Результат пожалуйста текстом на русском языке жирности и курсивность не делай вывод должен быть один
    """

    bot_msg_edit = await msg.answer(
        text=f"Отлично!\n\n✨ <b>Волшебство в процессе</b>! ⏳\n"
             f"@{msg.from_user.username}, ваша дата рождения принята! 🔢🎉",
        parse_mode="HTML"
    )

    await asyncio.sleep(2)
    await bot_msg_edit.edit_text(
        text="<i>Секундочку</i> — <i>запускаю нумерологический расчёт</i>... 📡\n",
        parse_mode="HTML"
    )

    send_ai = request_to_ai(request)

    await asyncio.sleep(1.8)
    await bot_msg_edit.edit_text(
        text="<i>Звёзды шепчут, числа танцуют — скоро откроем ваше Число Судьбы</i>! 🌟🔮",
        parse_mode="HTML"
    )

    await asyncio.sleep(1)
    await bot_msg_edit.edit_text(
        text="✨ <b>1...</b>",
        parse_mode="HTML"
    )

    await asyncio.sleep(1)
    await bot_msg_edit.edit_text(
        text="✨ <b>2...</b>",
        parse_mode="HTML"
    )

    await asyncio.sleep(1)
    await bot_msg_edit.edit_text(
        text="✨ <b>3...</b>",
        parse_mode="HTML"
    )

    await asyncio.sleep(1)
    await bot_msg_edit.edit_text(
        text="💫 <i>Ожидайте, магия уже на полпути</i>! 🚀",
        parse_mode="HTML"
    )

    await bot_msg_edit.delete()

    await msg.answer(
        send_ai,
        parse_mode="HTML",
        reply_markup=start_commands_buttons
    )