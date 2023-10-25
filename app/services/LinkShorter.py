from app.utils.generate_id import generate_short_id, generate_random_short_id
from db.database import redis


class LinkShortenerService:
    @staticmethod
    async def generate_short_link(link: str) -> str:
        link_id = await generate_short_id(link)
        # to avoid collision
        # if such link_id exists, generating random one
        while await redis.get(link_id):
            link_id = await generate_random_short_id()

        await redis.set(link_id, link)

        return link_id

    @staticmethod
    async def get_original_link(link_id: str):
        original_link = await redis.get(link_id)
        if original_link:
            return original_link
        return None

