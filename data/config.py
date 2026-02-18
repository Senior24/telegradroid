from environs import Env

env = Env()
env.read_env()

primary_lang = "en"

BOT_TOKEN = env.str("BOT_TOKEN")

DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_HOST = env.str("DB_HOST")
DB_NAME = env.str("DB_NAME")

OPEN_WEATHER_KEY = env.str("OPEN_WEATHER_KEY")
CEREBRAS_AI_KEY = env.str("CEREBRAS_AI_KEY")
