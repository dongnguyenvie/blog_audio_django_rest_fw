from django.conf.urls import url
from blogs.api.views import BlogListAPIView

urlpatterns = [
    url(r'^$', BlogListAPIView.as_view(), name='list'),
]
