from channels.generic.websocket import WebsocketConsumer
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