# Напишите функцию, которая принимает
# на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь,
# имя файла, расширение файла.

import os
def split_file_path(file_path):
    path, extension = os.path.splitext(file_path)
    dirname, name = os.path.split(path)
    return (dirname, name, extension)


if __name__ == "__main__":
    file_path = "/home/user/documents/report.txt"
    file_path2 = "/var/log/system.log"

    print(
        "Твой ответ",
        split_file_path(file_path),
        "Верный ответ - ('/home/user/documents', 'report', 'txt')"
    )

    print()

    print(
        "Твой ответ",
        split_file_path(file_path2),
        "Верный ответ - ('/var/log', 'system', 'log')"
    )
    