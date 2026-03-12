import aiohttp

from pydantic import TypeAdapter

from data.config import HACK_SEARCH_KEY

from .images import ImageSearchResponse
from .models import SearchResponse


api_url = "https://search.hackclub.com/res/v1/web/search"

async def get_websites(query: str) -> SearchResponse:
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url,
            params={"q": query},
            headers={'Authorization': f'Bearer {HACK_SEARCH_KEY}'}
                               ) as response:
            adapter = TypeAdapter(SearchResponse)
            print(await response.json())
            return adapter.validate_python(await response.json())
