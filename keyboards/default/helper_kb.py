from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

helper_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Как мне пройти?"),
            KeyboardButton(text="Отправить задание на сегодня"),
            KeyboardButton(text="Статистик за сегодня"),
        ],
        [
            KeyboardButton(text="Статистика по активным выставкам"),
            KeyboardButton(text="Результаты айтрекинга"),
        ]
    ]
)
