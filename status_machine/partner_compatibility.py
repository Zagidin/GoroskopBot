from aiogram.dispatcher.filters.state import (
    State,
    StatesGroup
)


class InfoPartner(StatesGroup):
    partner_one_name = State()
    partner_one_date_of_birth = State()

    partner_two_name = State()
    partner_two_date_of_birth = State()