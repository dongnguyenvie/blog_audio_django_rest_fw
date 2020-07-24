from django.conf.urls import url
from audio_src.apps.blogs.api.views import BlogListListView, BlogDetailsView

urlpatterns = [
    url(r'^(?P<pk>[0-9a-f-]+)/$', BlogDetailsView.as_view()),
    url(r'^$', BlogListListView.as_view(), name='list'),
]
