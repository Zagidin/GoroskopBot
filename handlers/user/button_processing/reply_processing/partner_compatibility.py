"""
    Совместимость с партнёром
"""

import asyncio

from random import choice
from ai.request_to_ai import request_to_ai
from bot.bot import dp
from aiogram.types import (
    Message,
    ReplyKeyboardRemove
)
from aiogram.dispatcher import FSMContext
from status_machine.partner_compatibility import InfoPartner
from keyboards.user.reply_buttons.start_buttons import start_commands_buttons


def verification_of_date_of_birth(user_data_of_birth):
    if user_data_of_birth:
        num_fate_partner = sum([int(num) for num in user_data_of_birth.replace(".", "")])

        while num_fate_partner > 9:
            num_fate_partner = sum([int(num) for num in str(num_fate_partner)])

        return num_fate_partner


@dp.message_handler(text="💞 Совместимость с партнёром или другом 💪")
async def partner_compatibility(msg: Message):
    await msg.answer(
        text=(
            "✨ <b>Откройте секреты совместимости с вашим 💪 другом / партнером</b> 💕\n\n"
            "📅 Введите даты рождения в таком формате: <b>дд.мм.гггг</b>\n"
            "Например: <b>17.08.2007</b>\n\n"
            "<i>Пусть судьба поможет вам понять друг друга!</i> 🔮"
        ),
        parse_mode="HTML",
        reply_markup=ReplyKeyboardRemove()
    )

    await msg.answer(
        text="Давайте начнем с Вас!\nКак вас зовут? ☺"
    )

    await InfoPartner.partner_one_name.set()


@dp.message_handler(state=InfoPartner.partner_one_name)
async def input_partner_one_name(msg: Message, state: FSMContext):

    async with state.proxy() as data:
        data["partner_one_name"] = msg.text

    await msg.answer(
        text="Отлично! Теперь введите имя друга / партнера 😉"
    )

    await InfoPartner.partner_two_name.set()


@dp.message_handler(state=InfoPartner.partner_two_name)
async def input_partner_two_name(msg: Message, state: FSMContext):

    async with state.proxy() as data:
        data["partner_two_name"] = msg.text

    await msg.answer(
        text="Хорошо! Теперь давайте узнаем вашу дату рождения, введите свою дату рождения в таком формате дд.мм.гггг ✍"
    )

    await InfoPartner.partner_one_date_of_birth.set()


@dp.message_handler(state=InfoPartner.partner_one_date_of_birth)
async def input_partner_one_data_birth(msg: Message, state: FSMContext):

    """
        💡 variable data["partner_one_fate"]: хранится число судьбы (1) первого партнера
    """

    async with state.proxy() as data:
        data["partner_one_fate"] = msg.text

        if data["partner_one_fate"]:
            if "." in data["partner_one_fate"][:3] and "." in data["partner_one_fate"][-5:]:
                if data["partner_one_fate"].replace(".", "").isdigit():
                    data["partner_one_fate"] = verification_of_date_of_birth(data["partner_one_fate"])
            else:
                await msg.answer(
                    text=f"Что-то пошло не так, некорректно набрана дата рождения, возможно вы не прописали разделительный знак \".\" ! "
                         f"Введите дату рождения по примеру {choice(['🤔', '😔'])}"
                )

    await msg.answer(
        text="Супер! Теперь в таком же формате дд.мм.гггг введите дату рождения друга / партнера 😉"
    )

    await InfoPartner.partner_two_date_of_birth.set()


@dp.message_handler(state=InfoPartner.partner_two_date_of_birth)
async def input_partner_two_data_birth(msg: Message, state: FSMContext):

    """
        💡 variable data["partner_two_fate"]: хранится число судьбы (2) второго партнера
    """

    async with state.proxy() as data:
        data["partner_two_data_birth"] = msg.text

        if data["partner_two_data_birth"]:
            if "." in data["partner_two_data_birth"][:3] and "." in data["partner_two_data_birth"][-5:]:
                if data["partner_two_data_birth"].replace(".", "").isdigit():
                    data["partner_two_fate"] = verification_of_date_of_birth(data["partner_two_data_birth"])

                    await state.finish()
            else:
                await msg.answer(
                    text=f"Что-то пошло не так, некорректно набрана дата рождения, возможно вы не прописали разделительный знак \".\" ! "
                         f"Введите дату рождения по примеру {choice(['🤔', '😔'])}"
                )

    prompt_ai = (
        f"Напишите вдохновляющий текст о совместимости {data['partner_one_name']} и {data['partner_two_name']}, "
        f"C Числами судьбы {data['partner_one_fate']} первого партнера, {data['partner_two_fate']} второго партнера,"
        f"Опишите их сильные стороны и то, как они могут дополнить друг друга. "
        f"Расскажите об их потенциале"
        f"Учти если будут мужские имена, то напиши о совместимости дружбы, а если мужской и женский то совместимости партнеров."
    )

    edit_bot_msg = await msg.answer(
        text=f"Прекрасно!\n\n✨ <b>Анализ совместимости начинается</b>! ⏳\n"
             f"@{msg.from_user.username}, даты рождения приняты! 🔢🎉",
        parse_mode="HTML"
    )

    await asyncio.sleep(2)
    await edit_bot_msg.edit_text(
        text="<i>Пожалуйста, подождите</i> — <i>запускаю анализ совместимости</i>... 📡\n",
        parse_mode="HTML"
    )

    send_ai = request_to_ai(prompt_ai)

    await asyncio.sleep(1.8)
    await edit_bot_msg.edit_text(
        text="<i>Сердца сближаются, числа сходятся — скоро мы откроем секреты вашей совместимости</i>! ❤️🔮",
        parse_mode="HTML"
    )

    await asyncio.sleep(1)
    await edit_bot_msg.edit_text(
        text="✨ <b>1...</b>",
        parse_mode="HTML"
    )

    await asyncio.sleep(1)
    await edit_bot_msg.edit_text(
        text="✨ <b>2...</b>",
        parse_mode="HTML"
    )

    await asyncio.sleep(1)
    await edit_bot_msg.edit_text(
        text="✨ <b>3...</b>",
        parse_mode="HTML"
    )

    await asyncio.sleep(1)
    await edit_bot_msg.edit_text(
        text="💫 <i>Не волнуйтесь, результаты уже на подходе</i>! 🚀",
        parse_mode="HTML"
    )

    await edit_bot_msg.delete()

    await msg.answer(
        send_ai,
        parse_mode="HTML",
        reply_markup=start_commands_buttons
    )
