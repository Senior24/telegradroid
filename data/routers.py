from handlers import start, new_topic, store, settings

routers_list = [
    start.router,
    new_topic.router,
    store.router,
    settings.router
]