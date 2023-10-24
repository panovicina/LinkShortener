from app.utils.generate_id import generate_short_id
from db.database import redis

class LinkShortenerService:
    @staticmethod
    async def generate_short_link(link: str) -> str:
        link_id = generate_short_id()
        await redis.set(link_id, link)
        return link_id

    @staticmethod
    async def get_link(link_id: str):
        original_link = await redis.get(link_id)
        return original_link
