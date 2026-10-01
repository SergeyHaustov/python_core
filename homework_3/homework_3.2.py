
def print_report(test_cases, statuses):
    report = list(zip(test_cases, statuses))
    print(report)
    fail_test = 0
    pass_test = 0
    length = len(statuses)
    for n in range(length):
        if statuses[n] == "PASS":
            pass_test += 1
        elif statuses[n] == "FAIL":
            fail_test += 1
        else:
            continue
    if fail_test > 0:
        print("The launch was unsuccessful.")

test_cases = ["Login", "Registration", "Checkout", "Logout"]
statuses = ["PASS", "FAIL", "PASS", "SKIP"]

print_report(test_cases, statuses)
