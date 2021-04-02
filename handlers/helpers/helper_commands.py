import time

from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards.default import helper_kb
from loader import dp, bot
from .helpers_id import helpers_id


@dp.message_handler(Text(equals="Я помощник"), state="*")
async def helper_login(message: types.Message):
    if message.from_user.id in helpers_id:
        await message.reply("Привет, как только появится задание, я отправлю его тебе")
        time.sleep(3)
        await bot.send_photo(chat_id=message.from_user.id, caption="Текущее задание:\n"
                                     "Найти экспонат ЛИМБ2020\n"
                                     "Измерить количество человек посетивших его с 14:00 поп 15:00\n"
                                     "Отправить мне овет цифрой", photo="https://disk.yandex.ru/i/JGufg780rYDMZQ")
    else:
        print('here')

@dp.message_handler(lambda message: message.text.isnumeric(), state="*")
async def response_to_number(message: types.Message):
    await message.reply("Спасибо за Вашу работу. Данные обрабатываются \n"
                        "Как только появится новое задание, я вам напишу")
