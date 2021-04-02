from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards.default import admin_kb
from loader import dp
from .list_of_admins import admins


@dp.message_handler(Text(equals="Я админ"), state="*")
async def admin_login(message: types.Message):
    if message.from_user.id in admins:
        await message.reply(f"Здраствуйте {message.from_user.username}! Вас я всегда узнаю) \n"
                            "Жду задания на сегодня.\n", reply_markup=admin_kb)


@dp.message_handler(Text(equals="Отправить задание на сегодня"),state="*")
async def admin_login(message: types.Message):
    if message.from_user.id in admins:
        await message.reply("Тут я запрошу у вас файл с заданиями и отправлю задания помошникам.\n"
                            "Я могу выбирать помошноков в случайном порядке или присваивать им задания исходя из нужной логики")


@dp.message_handler(Text(equals="Интерактивные графики"),state="*")
async def admin_login(message: types.Message):
    if message.from_user.id in admins:
        await message.reply("Тут будет красивая ссылки для перехода, но пока так\n"
                            "https://datalens.yandex/myrehgsa6f7sg?tab=qR&state=66a6b471216")


@dp.message_handler(Text(equals="Углубленный анализ отзывов"),state="*")
async def admin_login(message: types.Message):
    if message.from_user.id in admins:
        await message.reply("https://disk.yandex.ru/d/vPKQsWnsFekz4A?w=1")


@dp.message_handler(Text(equals="Анализ маршрутов посетителей"),state="*")
async def admin_login(message: types.Message):
    if message.from_user.id in admins:
        await message.reply("https://disk.yandex.ru/d/RpwtoldsctkBEw")

# @dp.message_handler(state="*")
# async def set_tasks(message: types.Message):
#     if message.from_user.id in admins:
#         await message.reply("Приму это сообщение как задание")
