from django.conf.urls import url
from audio_src.apps.categories.api.views import CategoryListAPIView, CategoryAPIView

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', CategoryAPIView.as_view()),
    url(r'^$', CategoryListAPIView.as_view(), name='list'),
]
