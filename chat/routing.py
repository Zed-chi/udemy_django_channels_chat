from django.conf.urls import url
from .consumers import ChatConsumer, AsyncChatConsumer, BaseSyncConsumer, BaseAsyncConsumer

urls = [
    url(r'^ws/chat/$', BaseAsyncConsumer),
    url(r'^ws/chat/(?P<room_name>\w+)/$', ChatConsumer),
]