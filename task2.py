# Напишите функцию, которая принимает
# на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь,
# имя файла, расширение файла.

# Пример 1:
# file_path1 = "/home/user/documents/report.txt"
# print(split_file_path(file_path1))
# ('/home/user/documents', 'report', 'txt')

# Пример 2:
# file_path2 = "/var/log/system.log"
# print(split_file_path(file_path2))
# ('/var/log', 'system', 'log')


def split_file_path(file_path):
    path = file_path[:(file_path.rfind('/'))]
    extention = file_path[(file_path.rfind('.') + 1):]
    file_name = file_path[(file_path.rfind('/') + 1):(file_path.rfind('.'))]
    result = path, file_name, extention
    return result


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
