import hashlib

import string

import random
from config.app_config import settings


async def generate_short_id(url: str):
    url_hash = hashlib.sha1(url.encode()).hexdigest()

    short_id = url_hash[:settings.SHORT_URL_LENGTH]
    return short_id


async def generate_random_short_id():
    characters = string.ascii_letters + string.digits
    short_id = ''.join(random.choice(characters) for _ in range(settings.SHORT_URL_LENGTH))

    return short_id
