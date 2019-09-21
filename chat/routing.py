from django.conf.urls import url
from .consumers import ChatConsumer

urls = [
    url(r'^ws/chat/$', ChatConsumer),
]