from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.default import main_kb
from keyboards.inline.callback_datas import exhibition_mode_callback, excursion_mode_callback, navigation_callback, \
    response_callback
from keyboards.inline.inline_kbs import excursion_duration_choice, inside_excursion_buttons, end_of_fast_track_excursion
from loader import bot
from loader import dp
from states.generalstate import GeneralState, Excursion


@dp.callback_query_handler(excursion_mode_callback.filter(choice_id='0'), state=GeneralState.Excursion)
async def exhibition_mode_selected(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=5)
    #data_ = await state.get_data()
    await Excursion.Starting.set()
    # await Excursion.Exhibit1.update_data(carried_on=data_)
    await bot.send_message(call.from_user.id, text="Из CSV куратора : Краткая инфа о выставке",
                           reply_markup=inside_excursion_buttons)


@dp.callback_query_handler(navigation_callback.filter(direction="end"), state=("*"))
async def end_of_excursion(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=5)
    await Excursion.End.set()
    await bot.send_message(call.from_user.id, "Поздравляем вы закончили маршрут Ключевые экспонаты",
                           reply_markup=end_of_fast_track_excursion)


@dp.callback_query_handler(navigation_callback.filter(direction="forward"), state=("*"))
async def forward_navigation(call: CallbackQuery, callback_data: dict, state: FSMContext):
    # print(await state.get_state())
    # print(type(await state.get_state())) #str
    if await state.get_state() == "Excursion:Starting":
        print("here")
    elif await state.get_state() == "Excursion:End":
        await bot.send_message(call.from_user.id,"Вы уже закончили экскурсию, проследуйте в Главное меню",reply_markup=main_kb)


@dp.callback_query_handler(response_callback.filter(), state=("*"))
async def like_dislike(call: CallbackQuery, callback_data: dict, state: FSMContext):
    if callback_data.get("choice_id") == "0":
        await call.answer("Ваш дизлайк был учтен",cache_time=5)
    else:
        await call.answer("Ваш like был учтен", cache_time=5)
