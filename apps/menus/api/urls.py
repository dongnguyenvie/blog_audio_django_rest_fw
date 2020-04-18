from django.conf.urls import url
from menus.api.views import MenuListAPIView

urlpatterns = [
    url(r'^$', MenuListAPIView.as_view(), name='list'),
]
