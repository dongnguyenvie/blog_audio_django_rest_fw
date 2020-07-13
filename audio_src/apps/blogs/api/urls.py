from django.conf.urls import url
from audio_src.apps.blogs.api.views import BlogListAPIView, BlogAPIView

urlpatterns = [
    url(r'^(?P<pk>[0-9a-f-]+)/$', BlogAPIView.as_view()),
    url(r'^$', BlogListAPIView.as_view(), name='list'),
]
