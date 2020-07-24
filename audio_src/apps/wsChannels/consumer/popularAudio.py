from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync
import json

dataMessages = []

class popularAudioConsumer(AsyncJsonWebsocketConsumer):
	async def connect(self):
		print('connect')
		await self.channel_layer.group_add("popular-audio", self.channel_name)
		print(f"Add {self.channel_name} channel to users's group")
		await self.accept()
		await self.send(text_data=json.dumps({
			'type': 'init',
			'messages': dataMessages
		}))


	async def disconnect(self, close_code):
		await self.channel_layer.group_discard("popular-audio", self.channel_name)
		print(f"Remove {self.channel_name} channel from users's group")
	
	async def receive(self, text_data):
		text_data_json = json.loads(text_data)
		message = text_data_json['message']
		print(f"receive {message}")
		
		await self.channel_layer.group_send("popular-audio", { 'type': 'chat_messageA', 'message': message })

	async def chat_messageA(self, event):
		print(f"event {event}")
		message = event['message']
		print(f"chat_message {message}")
		dataMessages.append(
			{'message':message}
		)
		await self.send(text_data=json.dumps({'message':message}))