correct_password = "Python123"

for i in range(3):
    user_password = input("Enter password: ")
    if user_password == correct_password:
        print("Success!")
        break
    elif i == 2:
        print("You blocked!")
