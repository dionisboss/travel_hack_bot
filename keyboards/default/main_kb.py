from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Главное меню"),
            KeyboardButton(text="Оставить отзыв"),
            KeyboardButton(text="Нужна помощь"),
        ],
    ]
)
