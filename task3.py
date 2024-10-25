# Напишите функцию, которая находит самое длинное слово в строке.

# Пример 1:
# sentence1 = "The quick brown fox jumped over the lazy dog"
# print(longest_word(sentence1))  # "jumped"

# Пример 2:
# sentence2 = "Python programming is fun"
# print(longest_word(sentence2))  # "programming"


def longest_word(sentence: str) -> str:
    res = '', 0
    for word in sentence.split(' '):
        if len(word) > res[1]:
            res = word, len(word)
    return res[0]


if __name__ == "__main__":
    sentence1 = "The quick brown fox jumped over the lazy dog"
    sentence2 = "Python programming is fun"

    print(
        "Твой ответ",
        longest_word(sentence1),
        "Верный ответ - jumped"
    )

    print()

    print(
        "Твой ответ",
        longest_word(sentence2),
        "Верный ответ - programming"
    )
