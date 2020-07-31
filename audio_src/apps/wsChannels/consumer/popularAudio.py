from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync
import json
from django.core.cache import cache
from functools import reduce

from audio_src.apps.utils import constants
from audio_src.apps.utils.constants import WS_TYPES


def getWachingStoryData():
    return cache.get(constants.TOP_WATCHING_STORY_KEY) or {}


def setTopWatchingStory(data={}):
    return cache.set(constants.TOP_WATCHING_STORY_KEY, data, timeout=None)


def getTopWachingStoryList(data):
    # return [article for article in sorted(data.values(), key=lambda article: article["view"])][:10]
    def userWatchingReduce(acc, cur):
        article = cur[1]
        try:
            index = list(map(lambda article: article['id'],
                             acc)).index(article["id"])
            _article = acc[index]
            acc[index] = {**_article, 'view': _article["view"] + 1}
        except ValueError:
            acc.append({**article, 'view': 1})
        return acc
    articleLst = reduce(userWatchingReduce, data.items(), [])
    return [article for article in sorted(articleLst, key=lambda article: article["view"])][:10]


WS_ACTIONS = WS_TYPES["ACTIONS"]


class popularAudioConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(constants.WS_POPULAR_AUDIO_GROUP, self.channel_name)
        # print(f"Connect::Add {self.channel_name} channel to users's group")
        await self.accept()
        await self.send(text_data=json.dumps({
            'clientType': WS_ACTIONS["QUERY_CONNECT_SETTINGS"],
            'payload': self.channel_name
        }))

    async def disconnect(self, close_code):
        idWs = self.channel_name
        await self.channel_layer.group_discard(constants.WS_POPULAR_AUDIO_GROUP, self.channel_name)
        # print(f"Remove {idWs} channel from users's group")
        await self.channel_layer.group_send(constants.WS_POPULAR_AUDIO_GROUP, {'type': 'action_update_unwatch_audio', 'data': idWs})

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        clientType = text_data_json.get("clientType")
        data = text_data_json.get("data")
        if clientType.startswith("WS_TYPES/WATCH/"):
            await self.channel_layer.group_send(constants.WS_POPULAR_AUDIO_GROUP, {'type': 'action_update_watch_audio', 'clientType': clientType, 'data': data})
        if clientType == WS_ACTIONS["QUERY_ALL_POPULAR_AUDIO"]:
            await self.channel_layer.group_send(constants.WS_POPULAR_AUDIO_GROUP, {'type': 'action_query_all_popular_audio'})

    async def action_update_watch_audio(self, event):
        userWatchingData = getWachingStoryData()
        data = event.get("data")
        clientType = event.get("clientType")
        articleWatching = userWatchingData.get(data['idWs'])
        if articleWatching:
            if clientType == WS_ACTIONS["TRACKING_WATCH_AUDIO"]:
                articleWatching = userWatchingData[data['idWs']] = data
        else:
            articleWatching = userWatchingData[data['idWs']] = data

        setTopWatchingStory(userWatchingData)
        topWachingStoryDataList = getTopWachingStoryList(userWatchingData)
        await self.send(text_data=json.dumps({'clientType': WS_ACTIONS["QUERY_ALL_POPULAR_AUDIO"], 'payload': topWachingStoryDataList}))

    async def action_update_unwatch_audio(self, event):
        userWatchingData = getWachingStoryData()
        idWs = event.get("data")
        articleUnwatching = userWatchingData.pop(idWs, None)
        setTopWatchingStory(userWatchingData)

        await self.send(text_data=json.dumps({'clientType': WS_ACTIONS["TRACKING_UNWATCH_AUDIO"], 'payload': articleUnwatching}))

    async def action_query_all_popular_audio(self):
        topWachingStoryData = getWachingStoryData()
        topWachingStoryDataList = getTopWachingStoryList(topWachingStoryData)
        await self.send(text_data=json.dumps({
            'clientType': WS_ACTIONS["QUERY_ALL_POPULAR_AUDIO"],
            'payload': topWachingStoryDataList
        }))
