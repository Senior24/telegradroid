import aiohttp

from pydantic import TypeAdapter

from data.config import OPEN_WEATHER_KEY

from .models import WeatherData

api_url = "https://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid={api_key}"

async def get_weather(city: str, units: str) -> WeatherData:
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url.format(city=city, units=units, api_key=OPEN_WEATHER_KEY)) as response:
            adapter = TypeAdapter(WeatherData)
            return adapter.validate_python(await response.json())
