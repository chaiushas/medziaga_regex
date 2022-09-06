import re


def cenzura(text, *swords):
    pattern = re.compile(r'(\w)(\w+)(\w)')
    for word in swords:
        grouped = pattern.search(word)
        censored = len(grouped.group(2)) * "*"
        censored_words = pattern.sub(f"\g<1>{censored}\g<3>", word)
        text = text.replace(word, censored_words)
    print(text)


cenzura('baisūs žodžiai, tokie kaip kvaraba, žaltys..', 'kvaraba', 'žaltys')