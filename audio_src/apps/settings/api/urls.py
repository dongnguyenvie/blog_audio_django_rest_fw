from django.conf.urls import url

from audio_src.apps.settings.api.views import SettingListView, SettingDetailsView

urlpatterns = [
    url(r'^(?P<pk>[0-9a-f-]+)/$', SettingDetailsView.as_view(), name='full'),
    url(r'^$', SettingListView.as_view(), name='list'),
]
