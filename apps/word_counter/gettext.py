from utils.gettext import _ as t_

def _(key: str, lang: str) -> str:
    return t_("word_counter_" + key, lang)
