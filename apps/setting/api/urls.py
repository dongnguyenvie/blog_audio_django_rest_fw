from django.conf.urls import url
from setting.api.views import SettingListAPIView

urlpatterns = [
    url(r'^$', SettingListAPIView.as_view(), name='list'),
]
