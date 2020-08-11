from django.conf.urls import url
from audio_src.apps.menus.api.views import MenuListView, MenuDetailsView

urlpatterns = [
    url(r'^(?P<pk>[0-9a-f-]+)/$', MenuDetailsView.as_view(), name='full'),
    url(r'^$', MenuListView.as_view(), name='list'),
]
