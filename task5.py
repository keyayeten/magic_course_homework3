# Напишите функцию, которая проверяет,
# являются ли две строки анаграммами
# (содержат одинаковые символы в разном порядке).

# Пример 1:
# str1_1 = "listen"
# str2_1 = "silent"
# print(are_anagrams(str1_1, str2_1))  # True

# Пример 2:
# str1_2 = "apple"
# str2_2 = "papel"
# print(are_anagrams(str1_2, str2_2))  # True

# Пример 3:
# str1_3 = "hello"
# str2_3 = "world"
# print(are_anagrams(str1_3, str2_3))  # False


def are_anagrams(str_1, str_2):
    res = True
    if len(str_1) != len(str_2):
        res = False
    else:
        l2 = list(str_2)
        for i in str_1:
            if i in l2:
                l2.remove(i)
            else:
                res = False
        if len(l2) != 0:
            res = False
    return res


if __name__ == "__main__":
    str1_1 = "listen"
    str2_1 = "silent"

    str1_2 = "apple"
    str2_2 = "papel"

    str1_3 = "hello"
    str2_3 = "world"

    print(
        "Твой ответ",
        are_anagrams(str1_1, str2_1),
        "Верный ответ - True"
    )

    print()

    print(
        "Твой ответ",
        are_anagrams(str1_2, str2_2),
        "Верный ответ - True"
    )

    print()

    print(
        "Твой ответ",
        are_anagrams(str1_3, str2_3),
        "Верный ответ - False"
    )
