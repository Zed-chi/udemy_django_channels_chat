from channels.routing import ProtocolTypeRouter, URLRouter
from chat.routing import urls


router = ProtocolTypeRouter({
    "websocket":URLRouter(
        urls
    )
})