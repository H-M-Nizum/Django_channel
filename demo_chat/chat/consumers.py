from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer

class MysynConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("connect consumer....", event)
        self.send({
            "type": "websocket.accept",
        })
    def websocket_receive(self, event):
        print("receive consumer....", event)
        self.send({
            "type": "websocket.send",
            "text": 'Salary deyna hala magir baccay. kmon r thakbo vi🥹🥹',
        })
    def websocket_disconnect(self, event):
        print("disconnect consumer....", event)
        raise StopConsumer()

# Geeky shows - 8
from time import sleep
from asgiref.sync import async_to_sync
class RealTimeDataConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("connect consumer....", event)
        print("channel layer,,,", self.channel_layer) # Get Default channels layer from a project
        print("Channels Name ,,,,", self.channel_name) # Get Default Channels Name from a project
        
        # Add a channel to a new or existing group
        async_to_sync(self.channel_layer.group_add)('Programmer', self.channel_name)
        
        self.send({
            "type": "websocket.accept",
        })
    def websocket_receive(self, event):
        print("receive consumer....", event)
        # for i in range(10):
        #     self.send({
        #         "type": "websocket.send",
        #         "text": str(i),
        #     })
        #     sleep(1)
        async_to_sync(self.channel_layer.group_send)('Programmer', {
            'type' : 'chat.message',
            'message' : event['text']
        })
    def websocket_disconnect(self, event):
        print("disconnect consumer....", event)
        async_to_sync(self.channel_layer.group_discard)('Programmer', self.channel_name)

        raise StopConsumer()

    def chat_message(self, event):
        print("client---", event)
        self.send({
            "type": "websocket.send",
            "text": event['message'],
        })

import asyncio        
class AsyRealTimeDataConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connect consumer....", event)
        await self.send({
            "type": "websocket.accept",
        })
    async def websocket_receive(self, event):
        print("receive consumer....", event)
        for i in range(10):
            await self.send({
                "type": "websocket.send",
                "text": str(i),
            })
            await asyncio.sleep(1)
    async def websocket_disconnect(self, event):
        print("disconnect consumer....", event)
        raise StopConsumer()



