from django.conf.urls import url
from audio_src.apps.medias.api.views import MediaDetailsView, MediaListListView

urlpatterns = [
    url(r'^(?P<pk>[0-9a-f-]+)/$',
        MediaDetailsView.as_view(), name='MediaDetailsView'),
    url(r'^$', MediaListListView.as_view(), name='MediaListListView'),
]
