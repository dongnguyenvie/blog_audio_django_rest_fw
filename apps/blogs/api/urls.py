from django.conf.urls import url
from blogs.api.views import BlogListAPIView, BlogAPIView

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', BlogAPIView.as_view()),
    url(r'^$', BlogListAPIView.as_view(), name='list'),
]
