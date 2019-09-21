from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from channels.consumer import SyncConsumer, AsyncConsumer
import json


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
    
    def disconnect(self, code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        message = data["message"]
        self.send(text_data=json.dumps({"answer":message}))


class AsyncChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
    
    async def disconnect(self, code):
        pass

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        message = data["message"]
        await self.send(text_data=json.dumps({"answer":message}))


class BaseSyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        self.send({"type":"websocket.accept"})
    
    def websocket_receive(self, event):
        self.send({
            "type":"websocket.send",
            "text":event['text']
        })


class BaseAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        await self.send({"type":"websocket.accept"})
    
    async def websocket_receive(self, event):
        await self.send({
            "type":"websocket.send",
            "text":event['text']
        })