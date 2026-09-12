"""5. Напишите программу, которая удаляет пробел в начале и в конце строки"""

variable_start = ' Какой-то текст для проверки программы с пробелами в конце и в начале '

print(len(variable_start))
variable_start = variable_start.strip()
print(len(variable_start))