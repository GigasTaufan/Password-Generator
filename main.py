import string
import random

def get_random_password():
    # random_set = string.ascii_letters + string.digits + string.punctuation
    random_set = string.ascii_letters + string.digits

    # lowercase
    password = random.choice(string.ascii_lowercase)

    # uppercase
    password += random.choice(string.ascii_uppercase)

    # digits
    password += random.choice(string.digits)

    # special characters
    # password += random.choice(string.punctuation)

    for i in range(4):
        password += random.choice(random_set)

    password_list = list(password)
    # shuffle all characters
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)

    return password


print("Password: ", get_random_password())
