from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default import main_kb
from keyboards.inline.inline_kbs import gen_exhibitions_inline_kb

from loader import dp
from loader import bot
from utils.mongo.user_class import User
from handlers.bot_dict import words_for_buttons
from states.generalstate import GeneralState


@dp.message_handler(Text(equals="Главное меню"), state='*')
@dp.message_handler(Text(equals="Я готов!"), state=None)
async def in_museum(message: types.Message):
    # set main menu state, so now
    await GeneralState.Main_menu.set()
    # from text and keyboards
    text = "Из CSV Куратора. Стартовый текст. Добро пожаловать"
    inline_kb = gen_exhibitions_inline_kb()
    # send message with proper menu kb
    await message.reply(text=text, reply_markup=inline_kb)
    await bot.send_message(chat_id=message.from_user.id,
                           text='Выберите интересующую Вас экскурсию из предложенные выше',
                           reply_markup=main_kb, disable_notification=True)
