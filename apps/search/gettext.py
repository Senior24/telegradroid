from utils.gettext import _ as t_

def _(key: str, lang: str) -> str:
    return t_(f"search_{key}", lang)