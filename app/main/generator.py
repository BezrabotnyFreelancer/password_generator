import random
import string

characters = list(string.ascii_letters + string.digits)


def generate_password(length: int):
    passwd = ''
    for i in range(length):
        passwd += random.choice(characters)

    return passwd

