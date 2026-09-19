number = 37
quantity = 0

while True:
    quantity += 1
    user_number = int(input("Enter a number: "))
    if number == user_number:
        print(f"Success! Number of attempts: {quantity}")
        break
    elif user_number < number:
        print("Your number is smaller.")
    elif user_number > number:
        print("Your number is greater.")