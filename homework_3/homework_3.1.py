
def get_test_statistics(results):
    fail_test = 0
    pass_test = 0
    skip_test = 0
    length =len(results)
    for n in range(length):
        if results[n] == "PASS":
            pass_test += 1
        elif results[n] == "FAIL":
            fail_test += 1
        elif results[n] == "SKIP":
            skip_test += 1
        else:
            continue
    return {"PASS": pass_test, "FAIL": fail_test, "SKIP": skip_test}

result = input("Enter result: ")
result = result.split()
dic_result = get_test_statistics(result)
quantity = sum(dic_result.values())
pass_rate = dic_result["PASS"] / quantity * 100
print(f"Всего тестов: {quantity} \nPASS: {dic_result["PASS"]} \nFAIL: {dic_result["FAIL"]} \nSKIP: {dic_result["SKIP"]} \nУспешно: {pass_rate}%")
