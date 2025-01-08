from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

from Callback.ElecticMeterCallback import ChooseElectricMeterCallback
from Model.ElectricMeterModel import ElectricMeter


def unpin_electricity_meter(username):
    inline_kb_list = []
    for electricMeter in ElectricMeter.select():
        inline_kb_list.append([
            InlineKeyboardButton(
                text=f"номер: {electricMeter.number} владелец: {electricMeter.owner}",
                callback_data=ChooseElectricMeterCallback(
                    number=electricMeter.number,
                    id=electricMeter.electric_meter_id,
                    owner=electricMeter.owner,
                    payer=electricMeter.payer,
                    username=username,
                ).pack())
        ])

    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)
