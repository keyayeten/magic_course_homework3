# Напишите функцию, которая проверяет,
# являются ли две строки анаграммами
# (содержат одинаковые символы в разном порядке).

def are_anagrams(str_1, str_2):
    str1_list = list(str_1)
    str1_list.sort()
    str2_list = list(str_2)
    str2_list.sort()
    return (str1_list == str2_list)


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
    