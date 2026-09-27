import json

try:
    with open('user_data.json', 'r', encoding='utf_8') as f:
        data = json.load(f)

        for n in range(len(data)):
            try:
                print(
                    f"Логин: {data[n]["login"]}\n"
                    f"Пароль: {data[n]["Password"]}\n"
                    f"Результат авторизации: {data[n]["AuthorizationResult"]}\n"
                )
            except KeyError as e:
                print(f"Ошибка в записи #: {n + 1}\n"
                      f"Отсутствует обязательное поле: {e}\n")

except FileNotFoundError:
    print(f"Файл не найден!")
except json.JSONDecodeError as e:
    print(f"Невозможно прочитать файл как JSON: {e}")
