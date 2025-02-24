from bot.bot import dp
from aiogram.utils.executor import start_polling


def start_bot():
    print("\033[32m\nБот Запущен!\033[0m")
    print("\033[34mАвтор: Zagidin Magamedragimov\033[0m")
    start_polling(
        dp,
        skip_updates=True
    )
    print("\033[33mБот остановлен!\033[0m")