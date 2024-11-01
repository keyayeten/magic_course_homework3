# Функция получает на вход словарь с названием компании
# в качестве ключа и списком с доходами и расходами (3-10 чисел)
# в качестве значения. Вычислите итоговую прибыль или убыток
# каждой компании. Если все компании прибыльные,
# верните истину, а если хотя бы одна убыточная - ложь.

def check_companies_profit(companies):
    all_profit = True

    for company, finances in companies.items():
        total = sum(finances)
        if total < 0:
            all_profit = False
    return all_profit


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
    