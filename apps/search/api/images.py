from pydantic import BaseModel
from typing import Optional


class ImageThumbnail(BaseModel):
    src: str
    width: int
    height: int


class ImageProperties(BaseModel):
    url: str
    placeholder: str
    width: int
    height: int


class ImageMetaUrl(BaseModel):
    scheme: str
    netloc: str
    hostname: str
    favicon: str
    path: str


class ImageResult(BaseModel):
    type: str
    title: str
    url: str
    source: str
    page_fetched: str
    thumbnail: ImageThumbnail
    properties: ImageProperties
    meta_url: ImageMetaUrl
    confidence: Optional[str] = None


class ImageQuery(BaseModel):
    original: str
    spellcheck_off: bool
    show_strict_warning: bool


class Extra(BaseModel):
    might_be_offensive: bool


class ImageSearchResponse(BaseModel):
    type: str
    query: ImageQuery
    results: list[ImageResult]
    extra: Optional[Extra] = None
