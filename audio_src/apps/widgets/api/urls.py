from django.conf.urls import url
from audio_src.apps.widgets.api.views import WidgetListAPIView, WidgetAPIView

urlpatterns = [
    url(r'^(?P<pk>[0-9a-f-]+)/$', WidgetAPIView.as_view(), name='full'),
    url(r'^$', WidgetListAPIView.as_view(), name='list'),
]
