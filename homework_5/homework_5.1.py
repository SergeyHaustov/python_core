from functools import reduce


def count_of_test_result(list_name, status):
    count_test = 0
    for n in range(len(list_name)):
        if list_name[n]["result"] == status:
            count_test += 1
    return count_test


test_list = [
    {"name": "Authorization", "result": "PASS", "execution time": 3.15},
    {"name": "Select item", "result": "SKIP", "execution time": 0.5},
    {"name": "Payment", "result": "PASS", "execution time": 5.73},
    {"name": "Turned on dark theme", "result": "PASS", "execution time": 11.0},
    {"name": "Check sum", "result": "FAIL", "execution time": 1.0},
    {"name": "Logout", "result": "FAIL", "execution time": 2.34},
]

count_failed_test = count_of_test_result(test_list, "FAIL")
count_pass_test = count_of_test_result(test_list, "PASS")
count_skip_test = count_of_test_result(test_list, "SKIP")

name_failed_test = list(map(lambda test: test["name"], filter(lambda test: test["result"] == "FAIL", test_list)))

name_pass_test = [test_list[n]["name"] for n in range(len(test_list)) if test_list[n]["result"] == "PASS"]

total_time = round(reduce(lambda total, time: total + time["execution time"], test_list, 0), 2)

print(
    f"Successful tests: {count_pass_test}\n"
    f"Failed tests:     {count_failed_test}\n"
    f"Skipped tests:    {count_skip_test}\n"
    f"Failed tests names:     {', '.join(name_failed_test)}\n"
    f"Successful tests names: {', '.join(name_pass_test)}\n"
    f"Total time:       {total_time}"
)
