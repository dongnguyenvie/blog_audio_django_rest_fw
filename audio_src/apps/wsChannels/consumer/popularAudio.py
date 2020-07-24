from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync
import json
from django.core.cache import cache

from audio_src.apps.utils import constants


def getTopWachingStory():
    return cache.get(constants.TOP_WATCHING_STORY_KEY)


def setTopWatchingStory(data):
    return cache.set(constants.TOP_WATCHING_STORY_KEY, data)


class popularAudioConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(constants.WS_POPULAR_AUDIO_GROUP, self.channel_name)
        print(f"Connect::Add {self.channel_name} channel to users's group")
        await self.accept()
        dataTopWachingStory = getTopWachingStory() or []

        await self.send(text_data=json.dumps({
            'type': 'init',
            'data': dataTopWachingStory
        }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(constants.WS_POPULAR_AUDIO_GROUP, self.channel_name)
        print(f"Remove {self.channel_name} channel from users's group")

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(f"receive {message}")

        await self.channel_layer.group_send(constants.WS_POPULAR_AUDIO_GROUP, {'type': 'set_top_watching_story', 'message': message})

    async def set_top_watching_story(self, event):
        await self.send(text_data=json.dumps({'message': message}))

    async def chat_messageA(self, event):
        print(f"event {event}")
        message = event['message']
        print(f"chat_message {message}")
        dataMessages.append(
            {'message': message}
        )
        await self.send(text_data=json.dumps({'message': message}))
