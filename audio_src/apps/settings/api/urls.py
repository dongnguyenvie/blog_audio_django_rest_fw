from django.conf.urls import url
from audio_src.apps.settings.api.views import SettingListAPIView, SettingAPIView

urlpatterns = [
    url(r'^(?P<pk>[0-9a-f-]+)/$', SettingAPIView.as_view(), name='full'),
    url(r'^$', SettingListAPIView.as_view(), name='list'),
]
