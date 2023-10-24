import aioredis

from config.app_config import settings


redis_url = f'{settings.REDIS_HOST}:{settings.REDIS_PORT}'
redis = aioredis.from_url(f'redis://{redis_url}', decode_responses=True)

