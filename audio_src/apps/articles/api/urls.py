from django.conf.urls import url
from audio_src.apps.articles.api.views import ArticleListView, ArticleDetailsView, ArticleDetailBySlugView

ArticleDetails = ArticleDetailsView.as_view()
ArticleList = ArticleListView.as_view()
ArticleDetailBySlug = ArticleDetailBySlugView.as_view()

urlpatterns = [
    url(r'^(?P<pk>[0-9a-f-]+)/$', ArticleDetails, name='ArticleDetails'),
    url(r'^(?P<slug>[\w_/-]+)/$', ArticleDetailBySlug,
        name='article_detail_slug'),
    url(r'^$', ArticleList, name='ArticleList'),
]
