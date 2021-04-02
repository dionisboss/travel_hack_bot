from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.callback_datas import exhibitions_callback, exhibition_mode_callback, excursion_mode_callback, \
    response_callback, navigation_callback, review_callback, G_coins_callback, excursion_statistics_callback


def gen_exhibitions_inline_kb():
    # get_active_exhibitions() ->list of dicts                  I need you to do this!!
    list_of_dicts_eg = [
        {
            "_id": "mongo_id",
            "exhibition_id": 'internal_id',
            "exhibition_name": "name"
        },
        {
            "_id": "mongo_id2",
            "exhibition_id": 'internal_id2',
            "exhibition_name": "name2",
        },
    ]
    # go through list and for buttons
    row_width = 2
    # # check if any name will be to big
    # for e in list_of_dicts_eg:
    #     if len(e['exhibition_name']) > 6:
    #         row_width = 2
    #         break
    # make kb
    kb_ = InlineKeyboardMarkup(row_width=row_width)
    for e in list_of_dicts_eg:
        if len(e['exhibition_name']) > 8:
            length = 8
        else:
            length = len(e['exhibition_name'])
        button = InlineKeyboardButton(
            text=e['exhibition_name'][0:length]+"...", callback_data=exhibitions_callback.new(
                exhibition_name=e['exhibition_name'],
                exhibition_id=e['exhibition_id'],
                db_exhibition_id=e['_id']
            )
        )
        kb_.insert(button)
    return kb_


exhibition_mode_choice = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Маршрут", callback_data=exhibition_mode_callback.new(choice_name="Маршрут", choice_id=0)),
        InlineKeyboardButton(text="Квиз", callback_data=exhibition_mode_callback.new(choice_name="Квиз", choice_id=1)),
        InlineKeyboardButton(text="Вольная птица", callback_data=exhibition_mode_callback.new(choice_name="Вольная птица", choice_id=2))
    ]
])

excursion_duration_choice = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="ключевые  экспонаты (30мин)", callback_data=excursion_mode_callback.new(choice_id=0)),
        InlineKeyboardButton(text=" все и сразу( 1 час)", callback_data=excursion_mode_callback.new(choice_id=1)),
        InlineKeyboardButton(text="полное погружение ( 1.5-2 ч)", callback_data=excursion_mode_callback.new(choice_id=2))
    ]
])

inside_excursion_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Идем", callback_data=navigation_callback.new(direction="forward")),
        InlineKeyboardButton(text="Закончить маршрут", callback_data=navigation_callback.new(direction="end")),
    ],
    [
                InlineKeyboardButton(text="Лайк", callback_data=response_callback.new(choice_id=1)),
                InlineKeyboardButton(text="Дизлайк", callback_data=response_callback.new(choice_id=0)),
    ]
])

end_of_fast_track_excursion = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Статистика посещения",
                             callback_data=excursion_statistics_callback.new(
                                 user_id="12345", excursion_id="1"
                             )),
        InlineKeyboardButton(text="Мои баллы", callback_data=G_coins_callback.new("get_current",0)),
    ],
    [
                InlineKeyboardButton(text="Написать отзыв!", callback_data=review_callback.new(user_id=12345, excursion_id=1)),
    ]
])
