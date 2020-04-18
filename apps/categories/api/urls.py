from django.conf.urls import url
from categories.api.views import CategoryListAPIView

urlpatterns = [
    url(r'^$', CategoryListAPIView.as_view(), name='list'),
]
