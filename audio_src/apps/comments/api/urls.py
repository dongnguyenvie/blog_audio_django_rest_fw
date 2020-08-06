from django.conf.urls import url

from audio_src.apps.comments.api.views import CommentDetailsView, CommentListView

urlpatterns = [
    url(r'^(?P<pk>[0-9a-f-]+)/$', CommentDetailsView.as_view(), name='full'),
    url(r'^$', CommentListView.as_view(), name='list'),
]
