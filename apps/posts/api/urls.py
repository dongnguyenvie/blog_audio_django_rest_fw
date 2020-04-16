from django.conf.urls import url
from posts.api.views import PostListAPIView

urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name='list'),
]
