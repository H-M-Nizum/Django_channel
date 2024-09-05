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
class RealTimeDataConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("connect consumer....", event)
        self.send({
            "type": "websocket.accept",
        })
    def websocket_receive(self, event):
        print("receive consumer....", event)
        for i in range(10):
            self.send({
                "type": "websocket.send",
                "text": str(i),
            })
            sleep(1)
    def websocket_disconnect(self, event):
        print("disconnect consumer....", event)
        raise StopConsumer()

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