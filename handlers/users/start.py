from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default import start_kb

from loader import dp
from loader import bot
from utils.mongo.user_class import User


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user_ = User(message.from_user.id).get_info()
    photo = "https://cdn-static-garagemca.gcdn.co/storage/tinymce_asset/1/5/1558/file-12d5f5db-d2bf-429c-888a-89e86a5209b4.gif"
    if user_:
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=photo,
                             caption=f"Рад снова Вас видеть, {user_['first_name']}!.\n"
                                     f"Если ты еще не в музее, то я могу подсказать"
                                     f"как до него добраться."
                                     f" Просто нажмите кнопку 'Как мне пройти?' \n"
                                     f"Или нажмите: 'Я готов!' и я проведу Вас по музею (сердечко)",
                             reply_markup=start_kb)
        User(message.from_user.id).update_last_active()
        # await message.reply(f"Рад снова Вас видеть, {user_['first_name']}!.\n"
        #                     f"Сегодня у нас (Выстака) выставка\n"
        #                     f"Провести вас по музею?", reply_markup=start_kb,)
    else:
        # add user to db with status started
        await message.reply(f"Привет, мы еще не знакомы {message.from_user.first_name}\n"
                            f"Я персональный ассистент-гид музея современного искусства - Гараж\n"
                            f"Я расскажу тебе о текущих выставках, смогу провести тебя по музею и "
                            f"подарю тебе специальный сувенир в конце посещения(тут вставить смайлик)")
        user_ = {
            "username": message.from_user.username,
            "first_name": message.from_user.first_name,
            "last_name": message.from_user.last_name,
        }
        if User(message.from_user.id).add_user(user_, message.text):
            await message.reply(f"Как будешь готов/a начать экскурсию нажми кнопку 'Начинаем'!\n"
                                f"Если ты еще не в музее, то я могу подсказать как до него добраться. "
                                f" Просто нажми кнопку 'Как мне пройти?'", reply_markup=start_kb)
        else:
            await message.reply(f"Произошла какая-то ошибка в моей работе. Я отправил ваш контакт администратору"
                                f", он скоро с вами свяжется (сердечко)")
            # сделать функцию для отправки ошибки админу


@dp.message_handler(Text(equals="Как мне пройти?"))
async def send_our_location(message: types.Message):
    await message.answer("Отправляю наши координаты. Как будете в музее, просто нажмите на кнопку:"
                         " 'Я готов!' и я проведу Вас по музею (сердечко) ")
    await bot.send_location(message.from_user.id, latitude=55.72781866500194,
                            longitude=37.60157183601152, live_period=1200, proximity_alert_radius=20)

#     # if user is registered but not active, try to activate
#     await message.answer(f'Привет, {message.from_user.full_name} {message.from_user.id}!')
#     user_info = dict(message.from_user)
#     print(dict(message.from_user))
#     await message.answer(f'вы ввели команду: {message.text}', reply_markup=main_menu)
#
# @dp.message_handler(content_types=types.ContentTypes.LOCATION)
# async def catch_coord(message: types.Message):
#     await message.answer("Я поймал вашу координату")
