# consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import Topic
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class TopicConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.topic_name = self.scope['url_route']['kwargs']['topic_name']
        self.topic_group_name = f'topic_{self.topic_name}'

        # Join the group
        await self.channel_layer.group_add(
            self.topic_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave the group
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

@receiver(post_save, sender=Topic)
def announce_new_comment(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f'topic_{instance.name}', 
            {
                'type': 'chat_message',
                'message': get_comments()
            }
        )