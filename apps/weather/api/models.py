from pydantic import BaseModel

from typing import List

class Coord(BaseModel):
    lon: float
    lat: float

class Weather(BaseModel):
    id: int
    main: str
    description: str
    icon: str

class Main(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    sea_level: int
    grnd_level: int
    wind_speed: int

class Wind(BaseModel):
    speed: float
    deg: int
    gust: float

class Clouds(BaseModel):
    all: int

class System(BaseModel):
    country: str
    sunrise: int
    sunset: int

class WeatherData(BaseModel):
    coord: Coord
    weather: List[Weather]
    base: str
    main: Main
    visibility: int
    wind: Wind
    clouds: Clouds
    dt: int
    sys: System
    timezone: int
    id: int
    name: str
    cod: int
