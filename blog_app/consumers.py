# consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import Topic
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class TopicConsumer(AsyncWebsocketConsumer):
    # Called when the websocket is handshaking as part of the connection process.
    async def connect(self):
        # Get the topic name from the URL
        self.topic_name = self.scope['url_route']['kwargs']['topic_name']
        self.topic_group_name = 'topic_%s' % self.topic_name

        # Join the topic group
        await self.channel_layer.group_add(
            self.topic_group_name,
            self.channel_name
        )

        # Accept the websocket connection
        await self.accept()

        # Announce the new user to everyone in the topic group
        await self.channel_layer.group_send(
            self.topic_group_name,
            {
                'type': 'user_join',
                'username': 'New User'
            }
        )

    # Called when the websocket closes for any reason.
    async def disconnect(self, close_code):
        # Leave the topic group
        await self.channel_layer.group_discard(
            self.topic_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.topic_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

    # Receive user join event from room group
    async def user_join(self, event):
        username = event['username']

        # Send join message to WebSocket
        await self.send(text_data=json.dumps({
            'message': f'{username} has joined the topic.'
        }))