from aiogram.utils.chat_action import ChatActionSender
from pyrogram.filters import bot

import config
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram import F

from Callback.ElecticMeterCallback import ChooseElectricMeterCallback
from Hendler.choiseElectricMeterHelper import choose_electric_meter
from Keyboard.menu import main_kb
from Keyboard.pinElectricMeter import pin_electricity_meter
from Keyboard.createQstInlineKb import create_qst_inline_kb
from Keyboard.questions import questions

from Hendler.getRandomUser import get_random_person
from Keyboard.unpinElectricMeter import unpin_electricity_meter

# Bot token can be obtained via https://t.me/BotFather
TOKEN = config.BOT_TOKEN

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer("Выберите один из пунктов меню. Что вы желаете сделать?", reply_markup=main_kb(message.from_user.id))


@dp.message(Command('faq'))
async def cmd_start_2(message: Message):
    await message.answer('Сообщение с инлайн клавиатурой с вопросами', reply_markup=create_qst_inline_kb(questions))


@dp.message(F.text.lower() == "закрепить за собой счетчик")
async def get_inline_btn_link(message: Message):
    await message.answer('Выберите счетчик для прикрепления!', reply_markup=pin_electricity_meter(message.from_user.username))


@dp.message(F.text.lower() == "открепить счетчик")
async def get_inline_btn_link(message: Message):
    await message.answer('Выберите счетчик для открепления!', reply_markup=unpin_electricity_meter(message.from_user.username))


@dp.callback_query(ChooseElectricMeterCallback.filter(F.id))
async def my_callback_foo(query: CallbackQuery, callback_data: ChooseElectricMeterCallback):
    await query.answer('test')
    choose_electric_meter(callback_data)


@dp.callback_query(F.data == 'get_person')
async def send_random_person(call: CallbackQuery):
    await call.answer('Генерирую случайного пользователя')
    user = get_random_person()
    formatted_message = (
        f"👤 <b>Имя:</b> {user['name']}\n"
        f"🏠 <b>Адрес:</b> {user['address']}\n"
        f"📧 <b>Email:</b> {user['email']}\n"
        f"📞 <b>Телефон:</b> {user['phone_number']}\n"
        f"🎂 <b>Дата рождения:</b> {user['birth_date']}\n"
        f"🏢 <b>Компания:</b> {user['company']}\n"
        f"💼 <b>Должность:</b> {user['job']}\n"
    )
    await call.message.answer(formatted_message)


@dp.callback_query(F.data.startswith('qst_'))
async def cmd_start_3(call: CallbackQuery):
    await call.answer()
    qst_id = int(call.data.replace('qst_', ''))
    qst_data = questions[qst_id]
    msg_text = f'Ответ на вопрос {qst_data.get("qst")}\n\n' \
               f'<b>{qst_data.get("answer")}</b>\n\n' \
               f'Выбери другой вопрос:'
    async with ChatActionSender(bot=bot, chat_id=call.from_user.id, action="typing"):
        await asyncio.sleep(1)
        await call.message.answer(msg_text, reply_markup=create_qst_inline_kb(questions))


# @dp.message()
# async def echo_handler(message: Message) -> None:
#     """
#     Handler will forward receive a message back to the sender
#
#     By default, message handler will handle all message types (like a text, photo, sticker etc.)
#     """
#     try:
#         # Send a copy of the received message
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         # But not all the types is supported to be copied so need to handle it
#         await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
