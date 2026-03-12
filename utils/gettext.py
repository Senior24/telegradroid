import yaml

from pathlib import Path

from data.config import PRIMARY_LANG

locales = {
    path.stem: yaml.safe_load(path.read_text(encoding="utf-8"))
    for path in Path('locales').glob('*.y*ml')
}


for app in Path("apps").iterdir():
    if app.name.startswith('_') or not app.is_dir():
        continue

    locales_dir = app / "locales"
    if not locales_dir.exists():
        continue

    for locale_file in locales_dir.iterdir():
        if locale_file.suffix not in {'.yaml', '.yml'}:
            continue

        lang = locale_file.stem
        content = yaml.safe_load(locale_file.read_text(encoding="utf-8"))

        if not content:
            continue

        locales[lang].update({
            f"{app.name}_{key}": value
            for key, value in content.items()
        })


def _(key: str, lang: str) -> str:
    if lang in locales.keys() and key in locales[lang].keys():
        return locales[lang][key]
    try:
        return locales[PRIMARY_LANG][key]
    except KeyError:
        return key
