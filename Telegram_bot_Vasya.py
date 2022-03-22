from aiogram import Bot, types, Dispatcher
from aiogram.utils import executor

import Keyboard
from Parsing.Api_weather import weather
from Parsing.Api_money import money
from config import TOKEN


bot = Bot(token=TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def bot_message(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        "Привет {0.first_name}, я Вася,"
        " нажми на кнопку и я дам тебе нужную информацию)".format(
            message.from_user),
        reply_markup=Keyboard.mainMenu,
    )


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == "Погода в Самаре":
        await bot.send_message(message.from_user.id, weather())
    elif message.text == "Курс валют":
        await bot.send_message(message.from_user.id, money())
    else:
        await bot.send_message(
            message.from_user.id,
            "{0.first_name}, Ничего не понятно, но очень интересно)".format(
                message.from_user
            ),
        )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
