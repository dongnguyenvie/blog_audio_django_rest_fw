from django.conf.urls import url
from posts.api.views import PostListAPIView, PostAPIView

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', PostAPIView.as_view()),
    url(r'^$', PostListAPIView.as_view(), name='list'),
]
