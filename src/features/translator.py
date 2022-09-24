import translators


def translate(text: str, src_lang: str = 'auto', target_lang: str = 'pl'):
    return translators.google(text, from_language=src_lang, to_language=target_lang)
