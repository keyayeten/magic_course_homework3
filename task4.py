# Напишите функцию, которая подсчитывает,
# сколько раз каждый элемент встречается в списке.
# Функция должна возвращать словарь с частотой каждого элемента.

def count_frequencies(lst):
    frequencies = {}
    for i in lst:
        if i in frequencies:
            frequencies[i] = frequencies[i] + 1
        else:
            frequencies[i] = 1
    return frequencies
        
    
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
    