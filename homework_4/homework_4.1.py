
with open("homework_4.1.1.txt","r") as file:
    digits = file.read().split()

length = len(digits)

if length <= 3:
    print("Error!")
else:
    print(digits[0])
    print(digits[1])
    print(digits[length-2])
    print(digits[length-1])
