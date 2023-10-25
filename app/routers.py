from fastapi import APIRouter, HTTPException
from app.services.LinkShorter import LinkShortenerService
from app.schemas import GetLinkResponse, CreateShortenedLinkResponse
router = APIRouter()


@router.post('/create', response_model=CreateShortenedLinkResponse)
async def create_shortened_link(url: str):
    id = await LinkShortenerService.generate_short_link(url)
    return CreateShortenedLinkResponse(id=id)


@router.get('/link/{id}', response_model=GetLinkResponse)
async def get_link(id: str):
    link = await LinkShortenerService.get_original_link(link_id=id)
    if link:
        return GetLinkResponse(link=link)

    raise HTTPException(status_code=404, detail="Link not found")
