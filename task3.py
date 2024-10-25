# Напишите функцию, которая находит самое длинное слово в строке.

# Пример 1:
# sentence1 = "The quick brown fox jumped over the lazy dog"
# print(longest_word(sentence1))  # "jumped"

# Пример 2:
# sentence2 = "Python programming is fun"
# print(longest_word(sentence2))  # "programming"


def longest_word(sentence):
    str1 = list(sentence.split(" "))

    longest_word = max(str1, key=len)

    return(longest_word)


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
