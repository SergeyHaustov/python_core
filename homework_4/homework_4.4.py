
with open("even_numbers.txt","r") as file:
    file_1 = file.read()

with open("odd_numbers.txt","r") as file:
    file_2 = file.read()

with open("even_numbers.txt","w") as file:
    file.write(file_2)

with open("odd_numbers.txt", "w") as file:
    file.write(file_1)
