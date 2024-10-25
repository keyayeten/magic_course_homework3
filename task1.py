# Функция получает на вход словарь с названием компании
# в качестве ключа и списком с доходами и расходами (3-10 чисел)
# в качестве значения. Вычислите итоговую прибыль или убыток
# каждой компании. Если все компании прибыльные,
# верните истину, а если хотя бы одна убыточная - ложь.

# Пример ввода:
# companies = {
#     "CompanyA": [1000, 200, -500, 300],
#     "CompanyB": [2000, -1000, 500],
#     "CompanyC": [3000, -1000, -3000]
# }

# Пример вывода:
# print(check_companies_profit(companies))  # False

# companies2 = {
#     "CompanyA": [1000, 200, 300],
#     "CompanyB": [2000, -1000, 500],
#     "CompanyC": [3000, -500, 500]
# }

# print(check_companies_profit(companies2))  # True


def check_companies_profit(companies):
    a = []
    for value in companies.values():
        a.append(sum(value))
        res = all(elem > 0 for elem in a)

    return res

if __name__ == "__main__":
    companies = {
        "CompanyA": [1000, 200, -500, 300],
        "CompanyB": [2000, -1000, 500],
        "CompanyC": [3000, -1000, -3000]
    }
    companies2 = {
        "CompanyA": [1000, 200, 300],
        "CompanyB": [2000, -1000, 500],
        "CompanyC": [3000, -500, 500]
    }

    print(
        "Твой ответ",
        check_companies_profit(companies),
        "Верный ответ - False"
    )

    print()

    print(
        "Твой ответ",
        check_companies_profit(companies2),
        "Верный ответ - True"
    )
