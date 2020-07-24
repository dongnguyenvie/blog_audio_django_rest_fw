from django.conf.urls import url

from audio_src.apps.tags.api.views import TagListView,  TagDetailsView

urlpatterns = [
    url(r'^(?P<pk>[0-9a-f-]+)/$', TagDetailsView.as_view(), name='full'),
    url(r'^$', TagListView.as_view(), name='list'),
]
