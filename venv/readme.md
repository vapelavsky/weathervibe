#WeatherVibes 0.1
####Created by KnoorTech

Can you imagine, what is sound of your weather? Our telegram bot can answer on this question.

WeatherVibes get information about weather in city which you send him, search in Spotify playlist for your weather and
send you weather information in chosen city and URL for Spotify playlist.

# Used libraries and APIs
1. Aiogram
2. Spotify Web API
3. OpenWeather API
4. Spotipy
5. Pyowm

#How to use?

1. git clone https://github.com/vapelavsky/weathervibe.git
2. cd weathervibe/
3. python3.8 -m venv venv
4. . venv/bin/activate
5. pip install -r requirements.txt
6. Fill config.py with Aiogram token, OWM token, SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET 
7. python bot.py