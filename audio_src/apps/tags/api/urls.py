from django.conf.urls import url

from audio_src.apps.tags.api.views import TagListView,  TagDetailsView, TagDetailsWithSlugView

urlpatterns = [
    url(r'^(?P<pk>[0-9a-f-]+)/$',
        TagDetailsView.as_view(), name='TagDetailsView'),
    url(r'^slug/(?P<slug>[\w_/-]+)/$', TagDetailsWithSlugView.as_view(),
        name='TagDetailsWithSlugView'),
    url(r'^$', TagListView.as_view(), name='TagListView'),
]
