# https://docs.aiogram.dev/en/stable/dispatcher/filters/callback_data.html
from aiogram.filters.callback_data import CallbackData


class ChooseElectricMeterCallback(CallbackData, prefix="electricityBill"):
    id: int
    number: int
    owner: str
    payer: str
    user_id: str
