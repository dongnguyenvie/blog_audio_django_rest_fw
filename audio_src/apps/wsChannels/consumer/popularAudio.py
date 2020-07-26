from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync
import json
from django.core.cache import cache

from audio_src.apps.utils import constants
from audio_src.apps.utils.constants import WS_TYPES


def getTopWachingStory():
    return cache.get(constants.TOP_WATCHING_STORY_KEY) or {}


def getTopWachingStoryList(data):
    return [article for article in sorted(data.values(), key=lambda article: article["view"])][:10]


def setTopWatchingStory(data={}):
    return cache.set(constants.TOP_WATCHING_STORY_KEY, data, timeout=120)


class popularAudioConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(constants.WS_POPULAR_AUDIO_GROUP, self.channel_name)
        print(f"Connect::Add {self.channel_name} channel to users's group")
        await self.accept()
        topWachingStoryData = getTopWachingStory()
        topWachingStoryDataList = getTopWachingStoryList(topWachingStoryData)

        await self.send(text_data=json.dumps({
            'clientType': WS_TYPES["POPULAR_AUDIO"],
            'topWachingStory': topWachingStoryDataList
        }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(constants.WS_POPULAR_AUDIO_GROUP, self.channel_name)
        print(f"Remove {self.channel_name} channel from users's group")

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        clientType = text_data_json.get("clientType")
        data = text_data_json.get("data")
        if (clientType == "receive_set_top_watching_story"):
            await self.channel_layer.group_send(constants.WS_POPULAR_AUDIO_GROUP, {'type': 'receive_set_top_watching_story', 'data': data})

    async def receive_set_top_watching_story(self, event):
        topWachingData = getTopWachingStory()
        data = event.get("data")
        article = topWachingData.get(data['id'])
        if article:
            print(article['view'])
            article = topWachingData[data['id']] = {
                **article,
                'view': article['view'] + 1
            }
        else:
            article = topWachingData[data['id']] = {
                **data,
                'view': 0
            }

        setTopWatchingStory(topWachingData)
        await self.send(text_data=json.dumps({'clientType': WS_TYPES["UPDATED_POPULAR_AUDIO"], 'data': article}))

    async def chat_messageA(self, event):
        print(f"event {event}")
        message = event['message']
        print(f"chat_message {message}")
        dataMessages.append(
            {'message': message}
        )
        await self.send(text_data=json.dumps({'message': message}))
