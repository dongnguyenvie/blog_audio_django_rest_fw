from rest_framework import generics, views, filters
from django.db import models
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework.response import Response

from audio_src.apps.articles.models import Article
from audio_src.apps.articles.api.serializers import ArticleSerializer
from audio_src.apps.utils.filters.extends import RelatedOrderingFilter
from audio_src.apps.articles.filters import ArticleFilter


class ArticleListView(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    ordering = ('?')

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, RelatedOrderingFilter]
    # filter_class = ArticleFilter
    filterset_fields = '__all__'
    ordering_fields = ('__all_related__')

    @method_decorator(cache_page(5))
    def list(self, *args, **kwargs):
        return super(ArticleListView, self).list(self, *args, **kwargs)

class ArticleDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class ArticleDetailBySlugView(generics.RetrieveAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'slug'
