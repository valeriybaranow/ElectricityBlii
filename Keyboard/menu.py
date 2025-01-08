from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def main_kb(user_telegram_id: int):
    kb_list = [
        [KeyboardButton(text="Закрепить за собой счетчик"), KeyboardButton(text="Открепить счетчик"),  KeyboardButton(text="👤 Ввести показания")],
        [KeyboardButton(text="📝 Оплатить"), KeyboardButton(text="📚 Увидеть показания счетчика")]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйтесь меню:"
    )
    return keyboard
