
with open("homework_4.1.1.txt","r") as file:
    digits = list(map(int, file.read().split()))

length = len(digits)
with open("even_numbers.txt","w") as file:
    for n in range(length):
        if digits[n] % 2 == 0:
            file.write(str(digits[n]))
            file.write(" ")

with open("odd_numbers.txt","w") as file:
    for n in range(length):
        if digits[n] % 2 != 0:
            file.write(str(digits[n]))
            file.write(" ")
