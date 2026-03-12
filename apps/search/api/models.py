from pydantic import BaseModel
from typing import Optional


class MetaUrl(BaseModel):
    scheme: str
    netloc: str
    hostname: str
    favicon: str
    path: str


class Thumbnail(BaseModel):
    src: str
    original: str
    logo: Optional[bool] = None


class Video(BaseModel):
    duration: Optional[str] = None
    creator: Optional[str] = None
    publisher: Optional[str] = None


class VideoResult(BaseModel):
    type: str
    url: str
    title: str
    description: Optional[str] = None
    age: Optional[str] = None
    page_age: Optional[str] = None
    fetched_content_timestamp: Optional[int] = None
    video: Optional[Video] = None
    meta_url: Optional[MetaUrl] = None
    thumbnail: Optional[Thumbnail] = None


class Videos(BaseModel):
    type: str
    results: list[VideoResult]
    mutated_by_goggles: Optional[bool] = None


class Profile(BaseModel):
    name: str
    url: str
    long_name: str
    img: str


class ClusterItem(BaseModel):
    title: str
    url: str
    is_source_local: bool
    is_source_both: bool
    description: str
    family_friendly: bool


class WebResult(BaseModel):
    title: str
    url: str
    is_source_local: bool
    is_source_both: bool
    description: str
    profile: Profile
    language: str
    family_friendly: bool
    type: str
    subtype: str
    is_live: bool
    meta_url: MetaUrl
    thumbnail: Optional[Thumbnail] = None
    cluster_type: Optional[str] = None
    cluster: Optional[list[ClusterItem]] = None
    extra_snippets: Optional[list[str]] = None
    age: Optional[str] = None
    page_age: Optional[str] = None


class Web(BaseModel):
    type: str
    results: list[WebResult]
    family_friendly: bool


class MixedItem(BaseModel):
    type: str
    index: Optional[int] = None
    all: bool


class Mixed(BaseModel):
    type: str
    main: list[MixedItem]
    top: list
    side: list


class Query(BaseModel):
    original: str
    show_strict_warning: bool
    is_navigational: bool
    is_geolocal: Optional[bool] = None
    local_decision: Optional[str] = None
    is_news_breaking: bool
    spellcheck_off: bool
    country: str
    bad_results: bool
    should_fallback: bool
    postal_code: str
    city: str
    header_country: str
    more_results_available: bool
    state: str


class SearchResponse(BaseModel):
    type: str
    query: Query
    mixed: Mixed
    videos: Optional[Videos] = None
    web: Web
