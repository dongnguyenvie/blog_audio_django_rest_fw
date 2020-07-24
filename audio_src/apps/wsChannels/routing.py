# myproject/routing.py
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from audio_src.apps.wsChannels.consumer.popularAudio import popularAudioConsumer

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
    	URLRouter(
    		[
    			path("popular-audio/", popularAudioConsumer),
    		]
    	)
    )
})
