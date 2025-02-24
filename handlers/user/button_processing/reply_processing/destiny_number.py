"""
    Число Судьбы
"""

import asyncio
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
             "\n📅 Введите дату рождения в любом удобном формате:\n"
             "    <i>\nНапример</i>:\n"
             "        <b>17 Августа 2007 года</b>\n"
             "\n<i>Пусть звёзды подскажут вашу уникальную дорогу!</i> 💫",
        parse_mode="HTML",
        reply_markup=ReplyKeyboardRemove()
    )

    await DateOfBirth.user_date_of_birth.set()

@dp.message_handler(state=DateOfBirth.user_date_of_birth)
async def user_date_of_birth_text(msg: Message, state: FSMContext):
    async with state.proxy() as data:
        data["user_date_of_birth"] = msg.text

    await state.finish()

    request = f"""
        Сгенерируй нумерологический отчёт на русском языке по дате рождения {data["user_date_of_birth"]}. 

        Шаг 1: Сложение всех цифр даты рождения
        Сначала складываем все цифры даты:
        
        Например Дата: 14.08.2004
        
        Сложение: 1+4+0+8+2+0+0+4=19
        
        Шаг 2: Приведение к однозначному числу
        Теперь сведём полученное число к однозначному:
        
        1+9=10
        
        Если ответ равен 10 и больше то складываем их тоже: 1+0=1
        
        Таким образом в данном примере, число судьбы даты — 1.
        
        По такой структере реши мою дату {data["user_date_of_birth"]}
        
        Решение как ты число вычисляешь, внимательно перепроверяй ответ и выводи ответ по структуре ниже 
            не надо что-то выдумывать или приделывать просто вычисление числа и вывод результата подходящий для этого числа.
    
        Структура Вывода сделай такую:
        🔢 Число Судьбы: число
         
        🧠 Влияние на личность: 1-2 предложения о характере
         
        🌟 Предназначение: Главная жизненная миссия 
        
        💡 Совет: Практическая рекомендация
    
        P.S можешь ещё от себя накидать информации интересной 😎
        Заранее спасибо! и Результат пожалуйста текстом на русском языке жирности и курсивность не делай вывод должен быть один
        Перед тем как вывести результат ещё раз перепроверь сложение чисел с даты!
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

    await bot_msg_edit.edit_text(
        send_ai,
        parse_mode="HTML"
    )

    await msg.answer(
        text="☝🤖",
        reply_markup=start_commands_buttons
    )