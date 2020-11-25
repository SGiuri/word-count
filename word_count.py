import re
from collections import Counter


def count_words(sentence):
    clear_sentence = re.sub(f"[^a-zA-Z0-9\']", " ", sentence)

    words = [word.strip("'").lower() for word in clear_sentence.split()]

    all_words = Counter(words)

    return all_words
