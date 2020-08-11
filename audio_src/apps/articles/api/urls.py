from django.conf.urls import url
from audio_src.apps.articles.api.views import ArticleListView, ArticleDetailsView, ArticleDetailsWithSlugView

ArticleDetails = ArticleDetailsView.as_view()
ArticleDetailsWithSlug = ArticleDetailsWithSlugView.as_view()
ArticleList = ArticleListView.as_view()
urlpatterns = [
    url(r'^(?P<pk>[0-9a-f-]+)/$', ArticleDetails, name='ArticleDetails'),
    url(r'^slug/(?P<slug>[\w_/-]+)/$', ArticleDetailsWithSlug,
        name='ArticleDetailsWithSlug'),
    url(r'^$', ArticleList, name='ArticleList'),
]
