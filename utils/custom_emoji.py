import aiohttp
import asyncio

from data.config import BOT_TOKEN

async def get_emoji_list():
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://api.telegram.org/bot{BOT_TOKEN}/getForumTopicIconStickers') as response:
            response = await response.json()
            return response['result']

emoji_list = asyncio.run(get_emoji_list())

def get_emoji_id(emoji: str) -> str | None:
    for target_emoji in emoji_list:
        if target_emoji['emoji'] == emoji:
            return target_emoji['custom_emoji_id']
    return None
