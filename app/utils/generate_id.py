import string
import random


def generate_short_id():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))