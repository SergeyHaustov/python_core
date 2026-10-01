import random

tests = [
    "test_login",
    "test_logout",
    "test_registration",
    "test_profile",
    "test_payment",
    "test_search"
]
result = [
    "PASS",
    "FAIL",
    "SKIP"
]

report = {}
quantity_test = int(input("Enter the number of tests: "))

if quantity_test > len(tests) or quantity_test == 0:
    print("Error! Incorrect number of tests!")
else:
    choose_test = random.sample(tests, k=quantity_test)
    for quantity in range(quantity_test):
        report[choose_test[quantity]] = random.choice(result)
    print(report)

