from django.conf.urls import url
from tags.api.views import TagListAPIView,  TagAPIView

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', TagAPIView.as_view(), name='full'),
    url(r'^$', TagListAPIView.as_view(), name='list'),
]
