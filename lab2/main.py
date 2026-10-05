import re
from collections import Counter
from typing import Optional


def split_words(text: str) -> list[str]:
    return re.findall(r"[^\W\d_]+", text.lower())


def count_word_frequencies(words: list[str]) -> dict[str, int]:
    return dict(Counter(words))


def top_word(freq: dict[str, int]) -> Optional[str]:
    return max(freq, key=freq.get, default=None)


print("Слова:", split_words(",д,д, ...д"))
print("Частоты:", count_word_frequencies(split_words(",д,д, ...д")))
print("Самое частое слово:", top_word(count_word_frequencies(split_words(",д,д, ...д"))))
