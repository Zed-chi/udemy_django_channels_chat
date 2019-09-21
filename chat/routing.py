from django.conf.urls import url
from .consumers import ChatConsumer, AsyncChatConsumer, BaseSyncConsumer

urls = [
    url(r'^ws/chat/$', BaseSyncConsumer),
]