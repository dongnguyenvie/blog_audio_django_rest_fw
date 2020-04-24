from django.conf.urls import url
from setting.api.views import SettingListAPIView, SettingAPIView

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', SettingAPIView.as_view(), name='full'),
    url(r'^$', SettingListAPIView.as_view(), name='list'),
]
