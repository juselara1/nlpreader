import pyperclip as _pyperclip
from nltk.tag import pos_tag as _pos_tag
from termcolor import colored

def get_words(text=None):
    if text is None:
        text = _pyperclip.paste()
    return [i for i in text.split(" ") if len(i) != 0]


def __make_colored(
        tagged_word,
        wpm, word_idx, total_words,
        colors, defaults
        ):
    word, tag = tagged_word
    color1 = colors["tags"][tag] if tag in colors["tags"] else colors["color1"]
    color2 = colors["color2"]
    color3 = colors["color3"]

    spacing = defaults["spacing"]
    if len(word) > 3:
        splits = [" "*(spacing), word[:2], word[2], word[3:], " "*(spacing - len(word[3:])) + f"WPM: {wpm}\tword: {word_idx}/{total_words}"]
    elif len(word) == 1:
        splits = [" "*(spacing + 2), "", word, "", " "*(spacing) + f"WPM: {wpm}\tword: {word_idx}/{total_words}"]
    elif len(word) == 2:
        splits = [" "*(spacing + 1), *(i for i in word), "", " "*(spacing) + f"WPM: {wpm}\tword: {word_idx}/{total_words}"]
    elif len(word) == 3:
        splits = [" "*(spacing + 1), *(i for i in word), " "*(spacing - 1) + f"WPM: {wpm}\tword: {word_idx}/{total_words}"]

    colors = [color1, color1, color2, color1, color3]
    *splits, = map(
            lambda x: colored(x[0], x[1]),
            zip(
                splits, colors
                )
            )
    return splits

def ner2color(
        words, wpm,
        colors, defaults
        ):

    tags = _pos_tag(words)
    return [
            __make_colored(
                tag, wpm,
                i + 1, len(tags),
                colors, defaults
                )
            for i, tag in enumerate(tags)
            ]
