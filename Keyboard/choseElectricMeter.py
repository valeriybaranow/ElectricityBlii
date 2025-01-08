from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

from Callback.ElecticMeterCallback import ChooseElectricMeterCallback
from Model.ElectricMeterModel import ElectricMeter


def ease_link_kb(user_id):
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
                    user_id=user_id,
                ).pack())
        ])

    # inline_kb_list = [
    #     [InlineKeyboardButton(text="Генерировать пользователя", callback_data='get_person')],
    #     [InlineKeyboardButton(text="Счетчик 2", url='tg://resolve?domain=yakvenalexx')],
    #     [InlineKeyboardButton(text="https://tg-promo-bot.ru/questions", web_app=WebAppInfo(url="https://tg-promo-bot.ru/questions"))]
    #     # [InlineKeyboardButton(text="На главную", callback_data='back_home')]
    # ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)
