from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import pyowm
from config import TOKEN, WTOKEN
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'uk'
owm = pyowm.OWM(WTOKEN, config_dict)
mgr = owm.weather_manager()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привіт!\nЯка би у тебе не була погода, ми допоможемо тобі підібрати музику.")


@dp.message_handler(commands=['start', 'help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


@dp.message_handler()
async def weather_message(message: types.Message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = round(w.temperature('celsius').get('temp'))  # Присваиваем переменной значение температуры из таблицы
    await message.answer(message.text + ": " + w.detailed_status + '\n\n' + "Температура: " + str(temp) + "℃")


if __name__ == '__main__':
    executor.start_polling(dp)
