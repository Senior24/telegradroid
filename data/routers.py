import os

from handlers import start, new_topic, store, settings, error

routers_list = [
    start.router,
    new_topic.router,
    store.router,
    settings.router,
    # error.router,
]

for app in os.listdir('apps'):
    module = __import__(f"apps.{app}.app", fromlist=["router"])
    routers_list.append(module.router)
