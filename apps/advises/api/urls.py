from django.conf.urls import url
from advises.api.views import AdviseListAPIView

urlpatterns = [
    url(r'^$', AdviseListAPIView.as_view(), name='list'),
]
