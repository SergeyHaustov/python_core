
with open("homework_4.3.1.txt","r+") as file:
    digits = list(map(int, file.read().split()))
    file.seek(0)
    length = len(digits)
    for length in range(length):
        digits[length] = digits[length] ** 2
    file.write(" ".join(map(str, digits)))
