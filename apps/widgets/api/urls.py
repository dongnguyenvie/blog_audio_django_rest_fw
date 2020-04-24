from django.conf.urls import url
from widgets.api.views import WidgetListAPIView, WidgetAPIView

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', WidgetAPIView.as_view(), name='full'),
    url(r'^$', WidgetListAPIView.as_view(), name='list'),
]
