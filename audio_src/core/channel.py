import django.core.management.commands.runserver as runserver
# cmd = runserver.Command()

ASGI_APPLICATION = 'audio_src.apps.wsChannels.routing.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}