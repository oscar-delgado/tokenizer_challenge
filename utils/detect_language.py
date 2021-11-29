from pycountry import languages as lang

from nltk import wordpunct_tokenize
from nltk.corpus import stopwords


def detect_language(text):
    """
    """
    lang_stopwords = {lang: set(stopwords.words(lang)) for lang in stopwords.fileids()}

    words = set(wordpunct_tokenize(text.lower()))
    matches = ((lang, len(words & stopwords)) for lang, stopwords in lang_stopwords.items())
    best_guess = max(matches, key = lambda match: match[1])

    return lang.get(name=best_guess[0]).alpha_2 if best_guess[1] > 0 else 'unknown'