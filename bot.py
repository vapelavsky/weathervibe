import pyowm
import spotipy
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils import executor
from emoji import emojize
from pyowm.utils.config import get_default_config

from config import TOKEN, WTOKEN, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = pyowm.OWM(WTOKEN, config_dict)
mgr = owm.weather_manager()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

button1 = KeyboardButton('/start')
button2 = KeyboardButton('/help')
button3 = KeyboardButton('/authors')

markup3 = ReplyKeyboardMarkup().add(button2).add(button3)
markup4 = ReplyKeyboardMarkup().add(button1).add(button3)
markup5 = ReplyKeyboardMarkup().add(button1).add(button2)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    if message.text == 'Получить настроение по погоде':
        await message.reply(emojize("Привет!\n\nКакая бы у тебя не была погода, мы поможем тебе подобрать музыку.\n\n"
                                    "Для этого достаточно написать название своего города - и ты получишь ссылку "
                                    "в Spotify на погодный плейлист :sparkling_heart:"), reply_markup=markup3)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    if message.text == 'Помощь':
        await message.reply("Напиши мне название своего города и я обязательно поделюсь с тобой музыкой по погоде!",
                            reply_markup=markup4)


@dp.message_handler(commands=['authors'])
async def authors_command(message: types.Message):
    if message.text == 'Авторы':
        await message.reply("Weather Vibes v0.1\n\nС любовью, KnoorTech :3", reply_markup=markup5)


@dp.message_handler()
async def weather_message(message: types.Message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = round(w.temperature('celsius').get('temp'))
    sp = spotipy.Spotify(client_credentials_manager=spotipy.SpotifyClientCredentials(SPOTIPY_CLIENT_ID,
                                                                                     SPOTIPY_CLIENT_SECRET))
    results = sp.search(w.detailed_status, type='playlist')
    items = results['playlists']['items']
    playlist = items[0]
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Настроение по погоде на Spotify",
                                            url=playlist['external_urls']['spotify'])
    keyboard.add(url_button)
    await message.answer(emojize(':sparkles: ') + message.text + ": " + w.detailed_status + '\n\n' +
                         emojize(':round_pushpin: ') + "Температура: " + str(temp) + "℃" + '\n\n' +
                         emojize(':musical_note: ') + "Плейлист, который идеально подойдёт: " + playlist['name'] +
                         '\n\n', reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp)
