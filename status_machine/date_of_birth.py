from aiogram.dispatcher.filters.state import (
    State,
    StatesGroup
)


class DateOfBirth(StatesGroup):
    user_date_of_birth = State()