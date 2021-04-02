import time

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import exhibitions_callback, exhibition_mode_callback
from keyboards.inline.inline_kbs import exhibition_mode_choice, excursion_duration_choice
from loader import bot
from loader import dp
from states.generalstate import GeneralState
from utils.mongo.user_class import User


@dp.callback_query_handler(exhibitions_callback.filter(), state=GeneralState.Main_menu)
async def exhibition_selected(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=5)
    # store data into state
    await state.update_data(exhibition_data=callback_data)
    user_: dict = User(call.from_user.id).get_info()
    # print(callback_data)
    # print(await state.get_data())
    if user_.get("skip_info") is True:
        await call.message.answer(f"Перевожу на выставку.")
    else:
        await GeneralState.Main_menu.set()
        await call.message.answer(f"Мы будем рады, если ты расскажешь о себе. "
                                  f"Так мы сможем сделать твой опыт в музее интереснее и понятнее"
                                  f"\n"
                                  f"Тут может начинаться блок соц дем вопросов"
                                  f"Включая привязвку карты друг музея\n\n\n")
    await GeneralState.Exhibition_start.set()

    text_choice = "Вы выбрали выставку (Название)\n" \
                  "(Описание)"
    picture_choice = 'https://thecomingworld.garagemca.org/img/gal-16.jpg'
    await bot.send_photo(chat_id=call.from_user.id, caption=text_choice, photo=picture_choice)
    text_ = 'У нас есть 3 формата посещения выставки: "маршрут", "квиз", "вольная птица". ' \
            'Маршрут - это готовый маршрут по выставке от наших кураторов. Квиз - это игровой формат в' \
            ' стиле квеста. Вольная птица -  подходи к объекту, пиши номер и получай лайфхаки и интересную инфу об объекте.' \
            ' Как будешь готов, выбирай'
    await bot.send_message(chat_id=call.from_user.id, text=text_, reply_markup=exhibition_mode_choice)


@dp.callback_query_handler(exhibition_mode_callback.filter(choice_id='0'), state=GeneralState.Exhibition_start)
async def exhibition_selected(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=5)
    await GeneralState.Excursion.set()
    await state.update_data(exhibition_mode=callback_data)
    text_ = "Выбери уровень :  ключевые  экспонаты (30мин), все и сразу( 1 час), полное погружение ( 1.5-2 ч)"
    await bot.send_message(chat_id=call.from_user.id, text=text_, reply_markup=excursion_duration_choice)
