# Напишите функцию, которая находит самое длинное слово в строке.

def longest_word(sentence):
    words = sentence.split()
    longest_words = max(words, key=len)
    return longest_words


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
    