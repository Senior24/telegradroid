from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")

PRIMARY_LANG = env.str("PRIMARY_LANG")

ADMINS = tuple(map(int, env.list("ADMINS")))

DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_HOST = env.str("DB_HOST")
DB_NAME = env.str("DB_NAME")

THEMED_GROUP_ID = env.int("THEMED_GROUP_ID")
ERRORS_THREAD_ID = env.int("ERRORS_THREAD_ID")
SUGGESTIONS_THREAD_ID = env.int("SUGGESTIONS_THREAD_ID")
REPORTS_THREAD_ID = env.int("REPORTS_THREAD_ID")
BUG_REPORTS_THREAD_ID = env.int("BUG_REPORTS_THREAD_ID")

OPEN_WEATHER_KEY = env.str("OPEN_WEATHER_KEY")
HACK_SEARCH_KEY = env.str("HACK_SEARCH_KEY")
CEREBRAS_AI_KEY = env.str("CEREBRAS_AI_KEY")
