from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Интерактивные графики"),
            KeyboardButton(text="Углубленный анализ отзывов"),
        ],
        [
            KeyboardButton(text="Анализ маршрутов посетителей"),
        ]
    ]
)
