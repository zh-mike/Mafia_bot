from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_default_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Создать новую игру")],
        [KeyboardButton(text="Присоединиться к игре")]
    ],
    resize_keyboard=True
)