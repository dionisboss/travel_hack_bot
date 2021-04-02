from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default import main_kb

from loader import dp
from loader import bot
from utils.mongo.user_class import User
from handlers.bot_dict import words_for_buttons
from states.user_state import User_state

@dp.message_handler(Text(equals="Главное меню"), state='*')
async def main_menu(message: types.Message, state: FSMContext):
    # finish state and set to main menu
    await state.finish()
    await User_state.Main_menu.set()
    text = "Из CSV Куратора. Стартовый текст. Добро пожаловать."
    inline_kb = 2
    # send message with proper menu kb
    await message.reply(text=text, reply_markup=main_kb)
