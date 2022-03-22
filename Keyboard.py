from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


button_weather = KeyboardButton("Погода в Самаре")
button_Exchange_rates = KeyboardButton("Курс валют")


mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button_weather, button_Exchange_rates
)
