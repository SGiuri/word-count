import re


def count_words(sentence):
    all_words = {}
    clear_sentence = re.sub(f"[^a-zA-Z0-9\']", " ", sentence)

    for word in clear_sentence.split():
        cleaner_lower_word = word.strip("'").lower()
        if cleaner_lower_word not in all_words.keys():
            all_words[cleaner_lower_word] = 1
        else:
            all_words[cleaner_lower_word] += 1

    return all_words
