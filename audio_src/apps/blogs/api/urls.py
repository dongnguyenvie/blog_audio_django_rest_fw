from django.conf.urls import url
from audio_src.apps.blogs.api.views import BlogListListView, BlogDetailsView, BlogDetailsWithSlugView

urlpatterns = [
    url(r'^(?P<pk>[0-9a-f-]+)/$',
        BlogDetailsView.as_view(), name='BlogDetailsView'),
    url(r'^slug/(?P<slug>[\w_/-]+)/$', BlogDetailsWithSlugView.as_view(),
        name='BlogDetailsWithSlugView'),
    url(r'^$', BlogListListView.as_view(), name='BlogListListView'),
]
