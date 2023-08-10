import json
from channels.generic.websocket import AsyncWebsocketConsumer
from pymongo import MongoClient
from bson.objectid import ObjectId
from asgiref.sync import async_to_sync

client = MongoClient()
db = client["Rengage"]
collection = db["channel"]

class DashboardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("notifications",self.channel_name)
        await self.send(
            text_data=json.dumps(
                {
                    "status": "conectado",
                }
            )
        )

    async def receive(self, text_data):
        message = json.loads(text_data) 
        notification = message["notification"]
        await print('aquiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
        await print(notification)
        await self.send(
            text_data=json.dumps(
                {
                    "type": "notification",
                    "message": notification,
                }
            )
        )
    async def send_notification(self, event):
        print('aaa')
        notification = event["message"]
        # message = json.loads(notification) 
        print(notification)
        await self.send(
            text_data=json.dumps(
                {
                    "type": "notification",
                    "message": notification,
                }
            )
        )