from pydantic import BaseModel, Field


class CreateShortenedLinkResponse(BaseModel):
    id: str = Field(..., description="The shortened link ID")


class GetLinkResponse(BaseModel):
    link: str = Field(..., description="The original link")