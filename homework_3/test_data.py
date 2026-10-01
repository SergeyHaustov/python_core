import random

def generate_login():
    login = str(random.randint(10000000, 99999999))
    return login

def generate_age():
    age = random.randint(18, 99)
    return age

def generate_status():
    status = ["ACTIVE", "BLOCKED","INACTIVE"]
    return random.choice(status)

def generate_user():
    user = {'Login': generate_login(), 'Age': generate_age(), 'Status': generate_status()}
    return user
