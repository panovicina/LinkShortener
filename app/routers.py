from fastapi import APIRouter
from app.services.LinkShorter import LinkShortenerService
router = APIRouter()


@router.post('/create', )
async def create_shortened_link(url: str):
    id = await LinkShortenerService.generate_short_link(url)
    return {"id": id}


@router.get('/link/{id}', )
async def get_link(id: str):
    link = await LinkShortenerService.get_link(link_id=id)
    #TODO: error
    return {'link': link}
