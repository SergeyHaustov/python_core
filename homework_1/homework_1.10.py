# Есть массив чисел. Известно, что каждое число в этом массиве имеет пару,
# кроме одного:
# [1, 5, 2, 9, 2, 9, 1] => 5
# Напишите программу, которая будет выводить уникальное число

digits = [1, 5, 2, 9, 2, 9, 1]
n = len(digits)
i = 0

for i in range(n):
    if digits[i] in digits[0:i] or digits[i] in digits[i+1:]:
        continue
    else:
        print(digits[i])


