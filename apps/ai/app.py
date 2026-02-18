from aiogram import F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from cerebras.cloud.sdk import Cerebras

from data.config import CEREBRAS_AI_KEY
from database.sql import db
from utils.gettext import _
from utils.modified_router import modified_router

router = modified_router("ai")

@router.message(CommandStart())
async def start(message: Message):
  lang = await db.lang(message.from_user.id)
  await message.answer(_("ai_start", lang))


@router.message(F.text)
async def generate_response(message: Message):
  lang = await db.lang(message.from_user.id)
  client = Cerebras(
    api_key=CEREBRAS_AI_KEY
  )

  try:
    completion = client.chat.completions.create(
      messages=[{"role":"user","content":message.text}],
      model="gpt-oss-120b",
      max_completion_tokens=1024,
      temperature=0.2,
      top_p=1,
      stream=False
    )

    await message.answer(completion.choices[0].message.content, parse_mode=ParseMode.MARKDOWN)
  except:
    await message.answer(_("ai_error", lang))
