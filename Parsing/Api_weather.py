import requests
import config


def get_api():
    lat = config.lat
    lon = config.lon
    api = config.api

    r = requests.get(
        f"https://api.openweathermap.org"
        f"/data/2.5/weather?"
        f"lat={lat}&lon={lon}&appid={api}&units=metric&lang=RU"
    )

    return r


def weather(r=get_api()):
    r = r.json()
    return (
        f'Самара, {r["weather"][0]["description"]}.\n'
        f'Температура: {r["main"]["temp"]} °С,\n'
        f'Ощущается как: {r["main"]["feels_like"]} °С.\n'
        f'Влажность воздуха: {r["main"]["humidity"]}%. \n'
        f'Ветер: {r["wind"]["speed"]} метр. в секунду.'
    )


weather()
