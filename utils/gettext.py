import os
import yaml

from data.config import primary_lang

locales = dict()

for locale in os.listdir('locales'):
    if locale.endswith(('.yaml', '.yml')):
        with open(f"locales/{locale}", "r", encoding="utf-8") as file:
            locale_lang = locale.split(".")[0]
            locales[locale_lang] = yaml.safe_load(file)

def _(key: str, lang: str) -> str:
    if lang in locales.keys() and key in locales[lang].keys():
        return locales[lang][key]
    try:
        return locales[primary_lang][key]
    except KeyError:
        return key
