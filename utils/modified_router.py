from aiogram import Router

from utils.filters import App

def modified_router(app: str) -> Router:
    router = Router()

    router.message.filter(App(app))
    router.callback_query.filter(App(app))
    router.edited_message.filter(App(app))
    router.poll.filter(App(app))
    router.poll_answer.filter(App(app))
    router.message_reaction.filter(App(app))
    router.edited_channel_post.filter(App(app))

    return router
