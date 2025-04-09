from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
)


start_commands_buttons = ReplyKeyboardMarkup(
    resize_keyboard=True
)

button_1 = KeyboardButton(
    text="🔮 Число Судьбы"
)
button_2 = KeyboardButton(
    text="💞 Совместимость с партнёром или другом 💪"
)
button_3 = KeyboardButton(
    text="💖 Число Души и Внутренние желания"
)

button_next = KeyboardButton(text="🚀 Дальше ➡️")

start_commands_buttons.row(
    button_1,
    button_2
)
start_commands_buttons.add(button_3)

start_commands_buttons.add(button_next) # Кнопка для перелистывания