import os
import yaml

locales = dict()

for locale in os.listdir('locales'):
    if locale.endswith(('.yaml', '.yml')):
        with open("locales", "r", encoding="utf-8") as file:
            lang = locale.split(".")[0]
            locales[lang] = yaml.safe_load(file)

def _(key: str, lang: str) -> str:

