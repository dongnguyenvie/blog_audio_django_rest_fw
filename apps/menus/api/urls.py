from django.conf.urls import url
from menus.api.views import MenuListAPIView, MenuAPIView

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', MenuAPIView.as_view(), name='full'),
    url(r'^$', MenuListAPIView.as_view(), name='list'),
]
