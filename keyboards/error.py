# from aiogram import Router, Bot, F
# from aiogram.filters import ExceptionTypeFilter
# from aiogram.types import ErrorEvent, Message
# from aiogram.fsm.context import FSMContext
#
# from data.config import THEMED_GROUP_ID, ERRORS_THREAD_ID
#
# from utils.database import db
# from utils.localization.get_text import _
#
# router = Router()
#
#
# @router.error(ExceptionTypeFilter(Exception))
# async def errors(event: ErrorEvent, state: FSMContext, bot: Bot):
#     full_name = event.update.message.from_user.full_name
#     user_id = event.update.message.from_user.id
#     lang = await db.lang(user_id)
#
#     msg = str()
#     msg += "Caused error: {error}\n".format(error=event.exception)
#     msg += "State: {state}\n".format(state=await state.get_state())
#     msg += "User: {user}\n".format(user=full_name)
#     msg += "ID: {id}\n".format(id=user_id)
#     msg += "User lang: {lang}".format(lang=lang)
#     await bot.send_message(chat_id=THEMED_GROUP_ID,
#                            message_thread_id=ERRORS_THREAD_ID,
#                            text=msg)
#     await event.update.message.answer(_("error", lang=lang))
