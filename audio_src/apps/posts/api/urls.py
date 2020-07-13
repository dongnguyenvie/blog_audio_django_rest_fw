from django.conf.urls import url
from audio_src.apps.posts.api.views import PostListView, PostDetailsView, PostTrendingListView

PostDetails = PostDetailsView.as_view()
PostList = PostListView.as_view()
PostTrendingList = PostTrendingListView.as_view()


urlpatterns = [
    url(r'^(?P<pk>[0-9a-f-]+)/$', PostDetails, name='PostDetails'),
    url(r'^$', PostList, name='PostList'),
    url('^trending/$', PostTrendingList, name='PostTrendingList'),
]
