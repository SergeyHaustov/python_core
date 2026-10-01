import test_data as users

active = 0
blocked = 0
inactive = 0
quantity_users = int(input("Enter the number of users: "))
list_users = []
for quantity in range(quantity_users):
    list_users.append(users.generate_user())
    print(list_users[quantity])
    if list_users[quantity]['Status'] == 'ACTIVE':
        active += 1
    elif list_users[quantity]['Status'] == 'BLOCKED':
        blocked += 1
    elif list_users[quantity]['Status'] == 'INACTIVE':
        inactive += 1

print(f"ACTIVE: {active} \nBLOCKED: {blocked} \nINACTIVE: {inactive}")
