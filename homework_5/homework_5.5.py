from functools import reduce
import json

tests_name = []
tests_status = []
tests_time = []
max_time = 0

def validate_required_fields(data):
    required_fields = {"Name", "Status", "Execution_time"}

    for index, test in enumerate(data):
        missing_fields = required_fields - test.keys()

        if missing_fields:
            raise ValueError(
                f"В элементе с индексом {index} отсутствуют обязательные поля: "
                f"{', '.join(sorted(missing_fields))}"
            )

def count_of_test_result(list_name, status):
    return sum(test["Status"] == status for test in list_name)


try:
    with open('test_data.json', 'r', encoding='utf_8') as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"Файл не найден!")
except json.JSONDecodeError as e:
    print(f"Невозможно прочитать файл как JSON: {e}")
else:
    try:
        validate_required_fields(data)
    except TypeError as e:
        print(f"Некорректная структура тестовых данных: {e}")
    else:
        for n in range(len(data)):
            if data[n]["Execution_time"] > max_time:
                max_time = data[n]["Execution_time"]
                longest_test = [data[n]["Name"], data[n]["Execution_time"]]

    failed_tests = filter(lambda test: test["Status"] == "FAIL", data)
    name_failed_test = [test["Name"] for test in failed_tests]
    total_time = round(reduce(lambda total, time: total + time["Execution_time"], data, 0), 2)

    failed_test = count_of_test_result(data, "FAIL")
    passed_test = count_of_test_result(data, "PASS")
    skipped_test = count_of_test_result(data, "SKIP")
    result_data = {
        "Total_number_of_test": len(data),
        "Passed_test": passed_test,
        "Failed_test": failed_test,
        "Skipped_test": skipped_test,
        "List_of_failed_tests": name_failed_test,
        "Longest_tests": longest_test,
        "Total_time": total_time
    }
    try:
        with open('test_result.json', 'w', encoding='utf_8') as f:
            json.dump(result_data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(e)
