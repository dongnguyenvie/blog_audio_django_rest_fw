import os

post = {
    'TYPE_OPTIONS': [
        (1, 'post'),
        (2, 'video'),
        (3, 'audio'),
        (4, 'image'),
        (5, 'other')
    ]
}

menu = {
    'TYPE_OPTIONS': [
        (1, 'header'),
        (2, 'sidebar-default'),
        (3, 'footer'),
        (4, 'main-nav'),
        (5, 'detail')
    ]
}

CACHE_TIME_TTL = os.getenv("CACHE_TIME_TTL") or 60 * 60

TOP_WATCHING_STORY_KEY = "TOP_WATCHING_STORY_KEY"

WS_POPULAR_AUDIO_GROUP = "WS_POPULAR_AUDIO_GROUP"

WS_TYPES = {
    "POPULAR_AUDIO": "POPULAR_AUDIO",
    "UPDATED_POPULAR_AUDIO": "UPDATED_POPULAR_AUDIO",
    "ACTIONS": {
        "QUERY_CONNECT_SETTINGS": "WS_TYPES/QUERY_CONNECT_SETTINGS",
        "QUERY_ALL_POPULAR_AUDIO": "WS_TYPES/WATCH/QUERY_ALL_POPULAR_AUDIO",
        "TRACKING_WATCH_AUDIO": "WS_TYPES/WATCH/TRACKING_WATCH_AUDIO",
        "TRACKING_UNWATCH_AUDIO": "WS_TYPES/WATCH/TRACKING_UNWATCH_AUDIO",
    }
}
