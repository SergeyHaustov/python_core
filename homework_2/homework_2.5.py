tests = {}
tests_fail = 0
tests_pass = 0
tests_skip = 0
quantity = int(input("Enter number of tests: "))

for i in range(quantity):
    tests[i] = input("Enter test status: ")
    if tests[i] == "FAIL":
        tests_fail += 1
    elif tests[i] == "PASS":
        tests_pass += 1
    elif tests[i] == "SKIP":
        tests_skip += 1

print(f"PASS tests: {tests_pass} \nFAIL tests: {tests_fail} \nSKIP tests: {tests_skip}")

if tests_fail > 0:
    print("There are FAIL tests.")
else:
    print("All tests are successful!")
