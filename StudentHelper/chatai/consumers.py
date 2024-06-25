from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer
import markdown
from . import google_ai_chat_control as gai

class MyAsyncChat(AsyncConsumer):
    async def websocket_connect(self, event):
        self.c = gai.sayhello()
        await self.send({
            'type':'websocket.accept',
        })

    async def websocket_receive(self, event):
        await self.send({
            'type':'websocket.send',
            'text':markdown.markdown(gai.askme(self.c, event['text']),extensions=['nl2br']),
        })

    async def websocket_disconnect(self, event):
        raise StopConsumer()

    