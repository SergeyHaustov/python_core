# Есть массив чисел. Известно, что каждое число в этом массиве имеет пару,
# кроме одного:
# [1, 5, 2, 9, 2, 9, 1] => 5
# Напишите программу, которая будет выводить уникальное число

digits = [1, 5, 2, 9, 2, 9, 1]
n = len(digits)

for i in range(n):
    if digits[i] not in digits[0:i] and digits[i] not in digits[i+1:]:
        print(digits[i])
