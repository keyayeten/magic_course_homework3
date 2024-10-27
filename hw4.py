# Напишите функцию, которая подсчитывает,
# сколько раз каждый элемент встречается в списке.
# Функция должна возвращать словарь с частотой каждого элемента.

# Пример 1:
# lst1 = [1, 2, 2, 3, 3, 3, 4]
# print(count_frequencies(lst1))
# {1: 1, 2: 2, 3: 3, 4: 1}

# Пример 2:
# lst2 = ['a', 'b', 'a', 'c', 'b', 'b', 'a']
# print(count_frequencies(lst2))
# {'a': 3, 'b': 3, 'c': 1}


def count_frequencies(lst):
    d = {}
    for i in lst:
        a = lst.count(i)
        d[i] = a
    return d



if __name__ == "__main__":
    lst1 = [1, 2, 2, 3, 3, 3, 4]
    lst2 = ['a', 'b', 'a', 'c', 'b', 'b', 'a']

    print(
        "Твой ответ",
        count_frequencies(lst1),
        "Верный ответ - {1: 1, 2: 2, 3: 3, 4: 1}"
    )

    print()

    print(
        "Твой ответ",
        count_frequencies(lst2),
        "Верный ответ - {'a': 3, 'b': 3, 'c': 1}"
    )