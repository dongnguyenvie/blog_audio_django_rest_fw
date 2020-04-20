from django.conf.urls import url
from posts.api.views import PostListAPIView

urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)(?P<pks>[0-9]+)/$', PostListAPIView.as_view(), name='list-none'),
]
