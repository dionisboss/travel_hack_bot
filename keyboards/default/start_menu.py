from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Я готов!"),
            KeyboardButton(text="Как мне пройти?"),
        ],
    ]
)

#
# start_kb = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text="Поделиться локацей", request_location=True),
#             KeyboardButton(text="Как мне пройти?"),
#         ]
#     ],
#     resize_keyboard=True
# )
